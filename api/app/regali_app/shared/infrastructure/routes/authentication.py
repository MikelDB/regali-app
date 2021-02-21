import os
from functools import wraps
import jwt

from flask import request, make_response
from flask_login import (
    LoginManager,
    login_required,
)

from werkzeug.security import generate_password_hash

from app import app
from app.regali_app.shared.application.use_cases import authentication
from app.regali_app.person.infrastructure.repositories.alchemy_person_repository import AlchemyPersonRepository
from app.regali_app.person.domain.exceptions.invalid_credentials_exception import InvalidCredentialsException

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

app.config['SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    use_case = authentication.GetUserUseCase()
    return use_case.execute(user_id)

@app.route('/login', methods=['GET'])
def login():
    use_case = authentication.RedirectToGoogleAuthenticationUseCase()
    return use_case.execute()


@app.route('/login/callback')
def login_callback():
    use_case = authentication.SigninOrSignupUserUseCase()
    return use_case.execute()


@app.route("/logout")
@login_required
def logout():
    use_case = authentication.LogoutUser()
    return use_case.execute()


def token_required(parent_function):
    @wraps(parent_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return   {'message': 'Token is missing'}, 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = AlchemyPersonRepository.find_one_by_public_id(data['public_id'])

        except jwt.ExpiredSignatureError:
            return {'message': 'token is invalid'}

        return parent_function(current_user, *args, **kwargs)
    return decorated


@app.route('/authentication/login', methods=['POST'])
def authenticate_login():
    auth = request.authorization
    try:
        use_case = authentication.UserLogin()
        token = use_case.execute(auth)

        return {'token' : token.decode('UTF-8')}
    except InvalidCredentialsException as exception:
        return make_response(exception.args[0], 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


@app.route('/authentication/register', methods=['POST'])
def authenticate_register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    use_case = authentication.UserRegister()

    use_case.execute(
        data['email'],
        data['name'],
        hashed_password
    )

    return {
        'message': 'User Created'
    }

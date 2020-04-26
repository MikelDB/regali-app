import os
from app import app
from flask_login import (
    LoginManager,
    login_required,
)
from app.usecases import authentication

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

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

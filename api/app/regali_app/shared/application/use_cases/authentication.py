import json
import os
import sys
import uuid
import jwt
from app import app, db
from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import requests
from app.regali_app.person.infrastructure.repositories.alchemy_person_repository import AlchemyPersonRepository
from app.regali_app.person.infrastructure.entities.alchemy_person import AlchemyPerson
from app.regali_app.person.domain.exceptions.invalid_credentials_exception import InvalidCredentialsException


# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)


login_manager = LoginManager()
login_manager.init_app(app)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

class GetUserUseCase():
    def execute(self, user_id):
        return AlchemyPersonRepository.find_one_by_user_id(user_id)

class RedirectToGoogleAuthenticationUseCase():
    def execute(self):
        google_provider_cfg = self.get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]

        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=request.base_url + "/callback",
            scope=["openid", "email", "profile"],
        )
        return redirect(request_uri)

    def get_google_provider_cfg(self):
        return requests.get(GOOGLE_DISCOVERY_URL).json()

class SigninOrSignupUserUseCase():
    def execute(self):
        # Get authorization code Google sent back to you
        code = request.args.get("code")

        google_provider_cfg = self.get_google_provider_cfg()
        token_endpoint = google_provider_cfg["token_endpoint"]

        # Prepare and send a request to get tokens! Yay tokens!
        token_url, headers, body = client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )

        # Parse the tokens!
        client.parse_request_body_response(json.dumps(token_response.json()))

        # Now that you have tokens (yay) let's find and hit the URL
        # from Google that gives you the user's profile information,
        # including their Google profile image and email
        userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
        uri, headers, body = client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        # You want to make sure their email is verified.
        # The user authenticated with Google, authorized your
        # app, and now you've verified their email through Google!
        if userinfo_response.json().get("email_verified"):
            unique_id = userinfo_response.json()["sub"]
            users_email = userinfo_response.json()["email"]
            picture = userinfo_response.json()["picture"]
            users_name = userinfo_response.json()["given_name"]
        else:
            return "User email not available or not verified by Google.", 400

        # Create a user in your db with the information provided
        # by Google

        user = AlchemyPersonRepository.find_one_by_google_id(google_id=unique_id)
        #user = models.Person.query.filter(models.Person.google_id == unique_id).first()

        # Doesn't exist? Add it to the database.
        if user is None:
            user = AlchemyPerson(id=None, google_id=unique_id, email=users_email, name=users_name, is_active=True, is_authenticated=True, profile_pic=picture)
            AlchemyPersonRepository.save(
                user
            )

        # Begin user session by logging the user in
        login_user(user)

        # Send user back to homepage
        return redirect(url_for("dashboard"))
    
    def get_google_provider_cfg(self):
        return requests.get(GOOGLE_DISCOVERY_URL).json()


class LogoutUser():
    def execute(self):
        logout_user()
        return redirect(url_for("index"))

class UserRegister():
    def execute(self, email, name, password):
        user = AlchemyPerson(
            None,
            str(uuid.uuid4()),
            None,
            name,
            email,
            True,
            True,
            'undefined',
            password
        )

        AlchemyPersonRepository.save(user)

class UserLogin():
    def execute(self, auth):
        if not auth or not auth.username or not auth.password:
            raise InvalidCredentialsException('Invalid Credentials, missing auth')

        user = AlchemyPersonRepository.find_one_by_email(auth.username)

        if not user:
            raise InvalidCredentialsException('Invalid Credentials, no user found')

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

            return token

        raise InvalidCredentialsException('Invalid Credentials, password won\'t match')
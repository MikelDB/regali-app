import os
from app import app
from flask_login import current_user
from flask import redirect, url_for


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
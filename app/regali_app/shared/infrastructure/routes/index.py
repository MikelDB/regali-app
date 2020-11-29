from flask_login import current_user
from flask import redirect, url_for

from app import app


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return '<a class="button" href="/login">Google Login</a>'


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

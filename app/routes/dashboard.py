from app import app
from flask import Flask, redirect, request, url_for, render_template
from flask_login import current_user, login_required


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')

"""Just to test if this eliminates the warning"""

# pylint: disable=wrong-import-position

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector


template_dir = os.path.abspath('regali_app/Shared/Infrastructure/presentation/templates')
template_dir2 = os.path.realpath('regali_app/Shared/Infrastructure/presentation/static')


app = Flask(__name__, template_folder='/app' + template_dir, static_folder='/app' + template_dir2)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.regali_app.shared.infrastructure.routes import routes

from app.regali_app.shared.infrastructure.dependency_injection.repositories import configure
from app.regali_app.shared.infrastructure.dependency_injection.domain_services import configure_services
from app.regali_app.shared.infrastructure.dependency_injection.use_cases import configure_use_cases
from app.regali_app.shared.infrastructure.dependency_injection.data_transformers import configure_data_transformers
from app.regali_app.shared.infrastructure.dependency_injection.factories import configure_factories

FlaskInjector(
    app=app,
    modules=[
        configure,
        configure_services,
        configure_use_cases,
        configure_data_transformers,
        configure_factories
    ]
)

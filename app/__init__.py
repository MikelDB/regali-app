import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector


template_dir = os.path.abspath('RegaliApp/Shared/Infrastructure/Presentation/templates')
template_dir2 = os.path.realpath('RegaliApp/Shared/Infrastructure/Presentation/static')

print('Template dir: ' + template_dir, file=sys.stdout)
print('Template dir2: ' + template_dir2, file=sys.stdout)

app = Flask(__name__, template_folder='/app' + template_dir, static_folder='/app' + template_dir2)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.RegaliApp.Shared.Infrastructure.Routes import routes

from app.RegaliApp.Shared.Infrastructure.DependencyInjection.Repositories import configure
from app.RegaliApp.Shared.Infrastructure.DependencyInjection.domain_services import configure_services
from app.RegaliApp.Shared.Infrastructure.DependencyInjection.use_cases import configure_use_cases
from app.RegaliApp.Shared.Infrastructure.DependencyInjection.data_transformers import configure_data_transformers

FlaskInjector(app=app, modules=[configure, configure_services, configure_use_cases, configure_data_transformers])
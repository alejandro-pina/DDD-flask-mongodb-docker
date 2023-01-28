from flask import Blueprint

auth = Blueprint("auth",__name__)

from .infractucture.routes import auth_public__route
from .infractucture.routes import auth_private__routes
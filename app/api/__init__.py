from flask import Blueprint
api = Blueprint("api",__name__)

from .user.infractucture.routes import user_private__routes
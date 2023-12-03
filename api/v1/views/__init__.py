#!/usr/bin/python3

"""

solution for task 3(views):

"""

from flask import Blueprint

app_views = Blueprint("api_v1", __name__, url_prefix="/api/v1")


from api.v1.views.index import*
from . import index
from api.v1.views.cities import*
from api.v1.views.amenties import*
from api.v1.views.places import*
from api.v1.views.users import*
from api.v1.views.states import*

#!/usr/bin/python3
""" Users Classes """
from models.base_model import BaseModel


class User(BaseModel):
    """ Users classes that inherits BaseModels """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

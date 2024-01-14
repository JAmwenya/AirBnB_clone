#!/usr/bin/python3
""" a module  that defines a city"""
from models.base_model import BaseModel
class City(BaseModel):
    """ class that creates a city"""
    state_id:str = ""
    name:str = ""

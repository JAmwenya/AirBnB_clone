#!/usr/bin/python3
from models.base_model import BaseModel
""" inherits from the parent class Basemodel"""
class User(BaseModel):
    """class attributes which are empty"""
    email:str = " "
    password: str = " "
    first_name: str = " "
    last_name: str = " "

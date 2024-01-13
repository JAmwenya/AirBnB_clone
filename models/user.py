#!/usr/bin/python3
""" module that inherits from the parent class Basemodel"""
from base_model import BaseModel
class User(BaseModel):
    """class attributes which are empty"""
    email:str = " "
    password: str = " "
    first_name: str = " "
    last_name: str = " "

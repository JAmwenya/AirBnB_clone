#!/usr/bin/python3
""" a module that definesa review"""
from models.base_model import BaseModel
class Review(BaseModel):
    """ a calss that creates the review"""
    place_id:str = ""
    user_id:str = ""
    text:str = ""

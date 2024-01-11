#!/usr/bin/python3
from models.base_model import BaseModel
""" a module that definesa review"""
class Review(BaseModel):
    """ a calss that creates the review"""
    place_id:str = " "
    user_id:str = " "
    text:str = " "

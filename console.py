#!/usr/bin/python3
""" entry point to the command interpreter"""
import cmd
#from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ command processor """
    prompt = "(hbnb) "
    __class = {
            "Basemodel",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State",
            "User"
            }
    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        """ Quit command to exit the program"""
        return True
    def do_empty(self, line):
        """
        does nothing when line is empty"""
        pass
     
    def do_create(self, line):
        lines = line.split()[0]
        if len(lines) == 0:
            print("** class name missing **")
        elif lines(0) not in HBNBCommand.__class:
            print("** class doesn't exist **")
        else:
            print(line(0).id())

if __name__ == '__main__':
    HBNBCommand().cmdloop()

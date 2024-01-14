#!/usr/bin/python3
""" 
entry point to the command interpreter
"""
import models
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import FileStorage
import json

class HBNBCommand(cmd.Cmd):
    """ 
    Command processor for the HBNB project
    """
    prompt = "(hbnb) "
    lastcmd = ""
    class_list = ["Amenity",
            "City",
            "Place",
            "Review",
            "State",
            "User",
            "Basemodel"]            

    def do_quit(self, line):
        """ 
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ 
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing when the line is empty
        """
        pass

    def do_create(self, line):
        """
        Creates an instance of BaseModel, saves it to a json file, and prints the id
        """
        lines = line.split()[0]
        if len(lines) == 0:
            print("** class name missing **")
        my_class = lines[0]
        if  my_class not in self.class_list:
            print("** class doesn't exist **")
        class_instance = eval(my_class)()
        class_instance.save()
        print(class_instance.id)

    def do_show(self, line):
        """ 
        Prints the string representation of an instance based on the class name and id
        """
        lines = line.split()[0]
        if len(lines) == 0:
            print("** class name missing **")
        my_class = lines[0]
        if  my_class not in self.class_list:
            print("** class doesn't exist **")
        if lines[1] == 1:
            print("** instance id missing **")
        my_id = lines[1]
        key = "{}.{}".format(my_class, my_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id and saves the changes
        """
        lines = line.split()[0]
        if len(lines) == 0:
            print("** class name missing **")
        my_class = lines[0]
        if  my_class not in self.class_list:
            print("** class doesn't exist **")
        if lines[1] == 1:
            print("** instance id missing **")
        my_id = lines[1]
        key = "{}.{}".format(my_class, my_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, line):
        """
        Prints all string representations of instances based on the class name or all instances
        """
        lines = line.split()[0]
        my_class = lines[0]
        if  my_class not in self.class_list:
           print("** class doesn't exist **")
        class_name = lines[0] if lines else None
        if class_name:
            instances = [
                    str(value) for key, value in models.storage.all().items() if key.startswith(class_name + ".")]
        else:
            instances = [
                    str(value) for key, value in
                    models.storage.all().items()
                    ]
        print(instances)

    def do_update(self, lines):
        """
        Updates an instance based on the class name and id by adding or updating an attribute
        """
        lines = lines.split()[0]
        if len(lines) == 0:
            print("** class name missing **")
        my_class = lines[0]
        if  my_class not in self.class_list:
           print("** class doesn't exist **")
        if lines[1] == 1:
            print("** instance id missing **")
        my_id = lines[1]
        key = "{}.{}".format(my_class, my_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(lines) < 3:
            print("** attribute name missing **")
            return
        attribute_name = lines[2]
        if len(lines) < 4:
            print("** value missing **")
            return
        attribute_value = lines[3]
        instance = models.storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()


#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    """
    entry point of the command interpreter

    """
    prompt = "(hbnb) "
    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True
    #alias
    do_EOF = do_quit

    #def do_EOF(self, line):
     #   """ Quit command to exit the program"""
      #  return True
    def do_empty(self, line):
        """
        does nothing when line is empty"""
        pass
     

if __name__ == '__main__':
    HBNBCommand().cmdloop()

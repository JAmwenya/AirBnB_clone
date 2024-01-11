import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Quite command to exit program"""
        return True
    #alias
    do_EOF = do_quit
    #def do_ls


if __name__ == '__main__':
    HBNBCommand().cmdloop()

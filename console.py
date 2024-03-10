#!/usr/bin/python3
""" Console module for AirBnB """
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command line interface."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def do_help(self, arg):
        """Help command to display help information."""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    """Start the command line interface."""
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
    Console module for AirBnB
    This module provides a command line interface for AirBnB
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Class for the command line interface.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
            Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
            Do nothing on empty input.
        """
        pass

    def do_help(self, arg):
        """Help command to display help information."""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    """Start the command line interface."""
    HBNBCommand().cmdloop()

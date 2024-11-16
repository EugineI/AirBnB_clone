#!/usr/bin/env python3
"""
The console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Starting the console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """(quit) to exit"""
        return True

    def do_EOF(self, line):
        """ (Ctrl + d) to exit."""
        print()
        return True

    def do_help(self, line):
        """ (help) list all the available commands"""
        if line == "quit":
            print("Quit command to exit the program")
        elif line == "EOF":
            print("Exit the program with EOF (Ctrl+D)")
        elif line == "help":
            print("Lists all the available commands")
        else:
            super().do_help(line)

    def emptyline(self):
        """handle empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

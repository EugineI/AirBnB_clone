#!/usr/bin/env python3
"""
The console
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Starting the console"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

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

    def do_create(self, line):
        """create instance of BaseModel."""
        if not line:
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[line]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show str representation of the instance."""
        parts = line.split()

        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = f"{parts[0]}.{parts[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, line):
        """Destroys an instance"""
        parts = line.split()
        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = f"{parts[0]}.{parts[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """str representation of all the instances"""
        if line and line not in self.classes:
            print("** class doesn't exist **")
            return
        instances = []
        for key, obj in storage.all().items():
            if not line or key.startswith(line):
                instances.append(str(obj))
        print(instances)

    def do_update(self, line):
        """update instance"""
        parts = line.split()
        if not parts:
            print("** class name missing **")
            return
        if parts[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        key = f"{parts[0]}.{parts[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(parts) < 3:
            print("** attribute name missing **")
            return
        if len(parts) < 4:
            print("** value missing **")
            return
        name = parts[2]
        value = parts[3]
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        else:
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass

        setattr(instance, name, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

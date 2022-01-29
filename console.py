#!/usr/bin/python
"""
The console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in classes_created:
                print("** class doesn't exist **")
            else:
                instance = classes_created[args[0]]()
                print(instance.id)
                instance.save()

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_created:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes_created:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = args.split()
        new = []
        if args == "":
            print("** class name missing **")
        if args[0] not in classes_created:
            print("** class doesn't exist **")
        if len(args) == 0:
            print(storage.all())
        else:
            for key in storage.all():
                new.append(str(storage.all()[key]))
            print(new)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

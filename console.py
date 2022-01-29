#!/usr/bin/python
"""
The console
"""
from datetime import datetime
import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {
    'Amenity': Amenity,'BaseModel': BaseModel , 'City':City,
    'Place': Place, 'Review': Review, 'State': State, 'User': User
}

list_of_classes = []
for key in classes:
    list_of_classes.append(key)


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
   
    def do_create(self, args):
        """Creates a new instance of BaseModel and saves it"""
        
        if args == "":
            print("** class name missing **")

        else:
            if args not in list_of_classes:
                print("** class doesn't exist **")
            else:
                new_instance = classes[args]()
                print(new_instance.id)
                new_instance.save()
    
    def do_show(self, args):
        """Prints string representation of an instance"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in list_of_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])
                        
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
      
        if args == "":
           print("** class name missing **")
        else:
           args = args.split()
           if args[0] not in list_of_classes:
               print("** class doesn't exist **")
           else:
               if len(args) < 2:
                   print("** instance id missing **")
               else:
                   key = args[0]+"." + args[1]
                   if key not in storage.all():
                       print("** no instance found **")
                   else:
                        del storage.all()[key]
                        storage.save()
                
    def do_all(self, args):
        """Prints string representation of all instances"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in list_of_classes:
                print("** class doesn't exist **")
            else:
                print(storage.all())
    
    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in list_of_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    instan_data = storage.all().get(key)
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(instan_data, args[2], args[3])
                                setattr(instan_data, 'updated_at', datetime.now())
                                storage.save()
            
           
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    
    
    
    
    
    

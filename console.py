#!/usr/bin/python3
"""
Command interpreter for the Holberton AirBnB project
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }
    ERR = [
        "** class name missing **",
        "** class doesn\'t exist **",
        "** instance id missing **",
        "** no instance found **",
        "** attribute name missing **",
        "** value missing **",
    ]

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program """
        return True

    def emptyline(self):
        """Called when an empty line is entered in the prompt """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id """
        args = arg.split()
        if len(args) < 1:
            print(HBNBCommand.ERR[0])
            return
        elif args[0] not in self.classes:
            print(HBNBCommand.ERR[1])
            return
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id """
        args = arg.split()
        if len(args) < 1:
            print(HBNBCommand.ERR[0])
            return
        if args[0] not in self.classes:
            print(HBNBCommand.ERR[1])
            return
        if len(args) < 2:
            print(HBNBCommand.ERR[2])
            return
        argid = args[0] + "." + args[1]
        if argid not in storage.all():
            print(HBNBCommand.ERR[3])
            return
        else:
            print(storage.all()[argid])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """
        args = arg.split()
        if len(args) < 1:
            print(HBNBCommand.ERR[0])
            return
        if args[0] not in self.classes:
            print(HBNBCommand.ERR[1])
            return
        if len(args) < 2:
            print(HBNBCommand.ERR[2])
            return
        argid = args[0] + "." + args[1]
        if argid not in storage.all():
            print(HBNBCommand.ERR[3])
            return
        else:
            storage.all().pop(argid)
            storage.save()

    def do_all(self, arg):
        """Prints all the string representation of all
        instances based or not on the class name """
        args = arg.split()
        all_list = []
        if not arg:
            for key in storage.all():
                all_list.append(storage.all()[key])
            print(list(map(str, all_list)))
            return
        else:
            if args[0] not in self.classes:
                print(HBNBCommand.ERR[1])
                return
            for key in storage.all():
                name = key.split('.')
                if name[0] == args[0]:
                    all_list.append(storage.all()[key])
            print(list(map(str, all_list)))

    def do_update(self, arg):
        """Updates an instance based on the class name and id """
        args = arg.split()
        if len(args) < 1:
            print(HBNBCommand.ERR[0])
            return
        if args[0] not in self.classes:
            print(HBNBCommand.ERR[1])
            return
        if len(args) < 2:
            print(HBNBCommand.ERR[2])
            return
        argid = args[0] + "." + args[1]
        if argid not in storage.all():
            print(HBNBCommand.ERR[3])
            return
        if len(args) < 3:
            print(HBNBCommand.ERR[4])
            return
        elif len(args) < 4:
            print(HBNBCommand.ERR[5])
            return
        else:
            obj = storage.all()[argid]
            if args[2] in obj.to_dict():
                setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
            else:
                setattr(obj, args[2], args[3])
            obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

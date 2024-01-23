#!/usr/bin/python3
""" console """

import cmd
import models
from datetime import datetime
from models.users import User
from models.base_model import BaseModel
from models.customers import Customer # , customer_item
from models.items import Item
from models.messages import Message
from models.procurements import Procurement
from models.payments import Payment
from models.services import Service
from models.invoice_services import Invoiced_service
from models.invoices import Invoice
from models.descriptions import Description
from models.described_items import Described_item
from models.deliverables import Deliverable
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DB_Storage
from colorama import init, Fore, Back, Style
import shlex  # for splitting the line along spaces except in double quotes

classes = {"User": User, "Item": Item, "Customer": Customer,
           "Deliverable": Deliverable, "Description": Description,
           "Described_item": Described_item, "Invoice": Invoice,
           "Invoiced_service": Invoiced_service, "Message": Message,
           "Payment": Payment, "Procurement": Procurement,
           "Service": Service } #, "customer_item": customer_item}


class DSEConsole(cmd.Cmd):
    """ DataStorageEngine console class"""
    prompt = Style.BRIGHT + Fore.YELLOW + "DataStorageEngine_EleFixStore:~ " + Style.RESET_ALL

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Bye")
        print("Thank you for using DSE Ele_Fix_Store")
        quit()

    def do_help(self, args):
        """it renders to users"""

    def emptyline(self):
        """cobtinue to next prompt"""
        pass

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_count(self, arg):
        """Count current number of class instances"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in DSEConsole.classes:
            print("** class doesn't exist **")
            return
        count = models.storage.count(class_name)
        print(count)

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_users", "settings", "data"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "User":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def handle_class_methods(self, arg):
        """Handle Class Methods  <cls>.all(), <cls>.show() etc"""
        print_ble = ("all(", "show(", "count(", "create(")
        try:
            evalu = eval(arg)
            for i in print_ble:
                if i in arg:
                    print(evalu)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            fld = te.args[0].split()[-1].replace("_", " ")
            fld = fld.strip("'")
            print(f"** {fld} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass


if __name__ == '__main__':
    DSEConsole().cmdloop()

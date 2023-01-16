#!/usr/bin/python3
"""
    base.py module
"""
import json
import csv


class Base:
    """ Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialitation method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None or list_objs == []:
            list1 = []
        with open(cls.__name__ + ".csv", "w") as fc:
            list_objs = [i.to_dictionary() for i in list_objs]
            rec = ['id', 'width', 'height', 'x', 'y']
            squ = ['id', 'size', 'x', 'y']
            if cls.__name__ == "Rectangle":
                f_csv = csv.DictWriter(fc, fieldnames=rec)
            else:
                f_csv = csv.DictWriter(fc, fieldnames=squ)
            f_csv.writeheader()
            f_csv.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances"""
        try:
            f = open(str(cls.__name__) + ".csv")
            f.close()
        except Exception:
            return []
        squ = ['id', 'size', 'x', 'y']
        rec = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle":
            fieldn = rec
        else:
            fieldn = squ

        inst = []
        with open(str(cls.__name__) + ".csv", "r") as fc:
            cr = csv.reader(fc, delimiter=',')
            for i, dictt in enumerate(cr):
                if i > 0:
                    ins = cls(1, 1)
                    for x, y in enumerate(dictt):
                        if y:
                            setattr(ins, fieldn[x], int(y))
                    inst.append(ins)
        return inst

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except Exception:
            return []

        list2 = []
        with open(str(cls.__name__) + ".json", "r") as f:
            list3 = cls.from_json_string(f.read())

        num_ins = len(l)
        inst = []
        for y in range(num_ins):
            inst.append(cls.create(**list2[y]))

        return inst

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None or list_objs == []:
            list4 = []
        else:
            list5 = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

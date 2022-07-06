import dataclasses


@dataclasses.dataclass
class DCModel:
    a: str
    b: str = None

    def __init__(self, **kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)


class Student:
    # class variables
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables
        print('Student:', self.name, self.age)
        # access class variables
        print('School:', self.school_name)

    @classmethod
    def change_school(cls, name):
        # access class variable
        print('Previous School name:', cls.school_name)
        cls.school_name = name
        print('School name changed to', Student.school_name)

    @staticmethod
    def find_notes():
        # can't access instance or class attributes
        print(['chapter 1', 'chapter 2', 'chapter 3'])


# create object
jessa = Student('Jessa', 12)
mike = Student('Mike', 14)
# call instance method
jessa.show()
jessa.change_school('XYZ')
mike.show()
jessa.find_notes()
mike.find_notes()

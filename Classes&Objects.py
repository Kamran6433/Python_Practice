# Classes in Python are blueprints for object creation.
# Classes can contain attributes or fields.
# the __init__(self) function is a constructor for the class and is called automatically
# to create an object of that class.
# self refers to the object that is to be created and acts like "this." in Java.
class Car:
    def __init__(self, name, model, year, real):
        self.name = name
        self.model = model
        self.year = year
        self.real = real

    def is_modern(self):
        if self.year >= 2015:
            return True
        else:
            return False

    def print_everything(self):
        return self.name, self.model, self.year, self.real


class ProgrammingLanguage:
    def __init__(self, difficulty, oop, curly_braces, do_i_like):
        self.difficulty = difficulty
        self.oop = oop
        self.curly_braces = curly_braces
        self.do_i_like = do_i_like

    def changed_my_mind(self, change):
        self.do_i_like = change

    def print_everything(self):
        return self.difficulty, self.oop, self.curly_braces, self.do_i_like


car1 = Car("Chiron", "Bugatti", 2019, True)
print(car1.name)
print("Car modern? " + str(car1.is_modern()))
print(car1.print_everything())

python = ProgrammingLanguage("Easy", True, False, True)
python.changed_my_mind(False)
print("Do I like this language? " + str(python.do_i_like))
print(python.print_everything())
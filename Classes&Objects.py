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


class ProgrammingLanguage:
    def __init__(self, difficulty, oop, curly_braces, do_i_like):
        self.difficulty = difficulty
        self.oop = oop
        self.curly_braces = curly_braces
        self.do_i_like = do_i_like

    def changed_my_mind(self, change):
        self.do_i_like = change


car1 = Car("Chiron", "Bugatti", 2019, True)
print(car1.name)
print("Car modern? " + str(car1.is_modern()))

python = ProgrammingLanguage("Easy", True, False, True)
python.changed_my_mind(False)
print("Do I like this language? " + str(python.do_i_like))
# Inheritance allows us to have a class that takes all the methods adn attributes from another class.
# PARENT CLASS is the class that will give its methods and attributes to its CHILD CLASS.
# CHILD CLASS is the class that takes the methods and attributes from the PARENT CLASS.

# PARENT CLASS:
class Vehicle:
    def __init__(self, model, wheels, doors, engine):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.engine = engine

    def rev_engine(self, engine):
        if engine:
            print("The engine is revving!")
        else:
            print("This vehicle doesn't have an engine.")

    def spin_wheel(self, wheels):
        if wheels > 0:
            print("The wheels are spinning!")
        else:
            print("This vehicle has no wheels.")

    def open_doors(self, doors):
        if doors:
            print("The doors are all open!")
        else:
            print("This vehicle doesn't have doors.")


# CHILD CLASSES:
class Car(Vehicle):
    def __init__(self, model, wheels, doors, engine, horsepower):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.horsepower = horsepower


class ElectricCar(Vehicle):
    def __init__(self, model, wheels, doors, engine, motor_power):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.motor_power = motor_power


class MotorCycle(Vehicle):
    def __init__(self, model, wheels, doors, engine, horsepower):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.horsepower = horsepower


class Titanic(Vehicle):
    def __init__(self, model, wheels, doors, engine, weight):
        self.model = model
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.weight = weight
        
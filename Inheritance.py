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

    def rev_engine(self):
        if self.engine:
            print("The engine is revving!")
        else:
            print("This vehicle doesn't have an engine.")

    def spin_wheel(self):
        if self.wheels > 0:
            print("The wheels are spinning!")
        else:
            print("This vehicle has no wheels.")

    def open_doors(self):
        if self.doors:
            print("The doors are all open!")
        else:
            print("This vehicle doesn't have doors.")


# CHILD CLASSES:
class Car(Vehicle):
    def __init__(self, model, wheels, doors, engine, horsepower):
        super().__init__(model, wheels, doors, engine)
        # To inherit you must use the super method to reference the parent and fill the constructor with
        # the parent's attributes.
        # You can then add the child's attributes above it.
        # You don't need to use self.parents_attribute as it's inheriting the parent's attributes.
        self.horsepower = horsepower


class ElectricCar(Vehicle):
    def __init__(self, model, wheels, doors, engine, motor_power):
        super().__init__(model, wheels, doors, engine)
        self.motor_power = motor_power


class MotorCycle(Vehicle):
    def __init__(self, model, wheels, doors, engine, horsepower):
        super().__init__(model, wheels, doors, engine)
        self.horsepower = horsepower


class Titanic(Vehicle):
    def __init__(self, model, wheels, doors, engine, weight_in_tonnes):
        super().__init__(model, wheels, doors, engine)
        self.weight_in_tonnes = weight_in_tonnes


car = Car("Lamborghini", 4, 3, True, 600)
electric_car = ElectricCar("Tesla", 4, 5, False, 700)
motor_cycle = MotorCycle("Suzuki", 2, 0, True, 350)
titanic = Titanic("Titanic", 0, 150, True, 5)

car.rev_engine(), car.open_doors(), car.spin_wheel()
electric_car.rev_engine(), electric_car.open_doors(), electric_car.spin_wheel()
motor_cycle.rev_engine(), motor_cycle.open_doors(), motor_cycle.spin_wheel()
titanic.rev_engine(), titanic.open_doors(), titanic.spin_wheel()
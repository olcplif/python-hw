# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method
class Bus(Vehicle):
    def __init__(self, capacity, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f"Capacity of the Bus = {self.capacity}")


# 3. Determine which class a given Bus object belongs to (Check type of an object)
mercedes = Bus(50, 140, 500000)
print("Type of an object -", type(mercedes))

# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus(55, 70, 355000)
print("School_bus is instance of Vehicle class -", isinstance(School_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own -
# bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, color, get_school_id, number_of_students, capacity, max_speed, mileage):
        super().__init__(get_school_id, number_of_students, capacity, max_speed, mileage)
        self.color = color

    def bus_school_color(self):
        pass


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.


class Bear:
    def make_sound(self):
       print('Grrrr')


class Wolf:
    def make_sound(self):
        print('Owooo')


bear = Bear()
wolf = Wolf()
animals = (bear, wolf)

for animal in animals:
    animal.make_sound()

# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def check_population(self):
        if self.population > 1500:
            return f'The population of the city {self.name} is {self.population}'
        else:
            return 'Your city is too small'


ivano_frankivsk = City("Ivano-Frankivsk", 25000)
mykytynci = City("Mykytynci", 1000)
print(ivano_frankivsk.check_population())
print(mykytynci.check_population())

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.


class Addition:
    def __init__(self, addition):
        self.addition = addition

    def __add__(self, other):
        if self.addition > 10 or other.addition > 10:
            return self.addition * other.addition
        else:
            return self.addition + other.addition


x = Addition(11)
y = Addition(10)
add = x + y
print(add)


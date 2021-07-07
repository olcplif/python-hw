# #1. Make the class with composition.
class Laptop:
    def __init__(self):
        battery1 = Battery(10000)
        battery2 = Battery(15000)
        self.batteries = [battery1, battery2]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()
print(laptop)
# OUTPUT: <__main__.Laptop object at 0x7f4aad1b4070>
print(laptop.batteries)


# OUTPUT: [<__main__.Battery object at 0x7f4aad175a30>, <__main__.Battery object at 0x7f4aad175be0>]


# #2. Make the class with aggregation
class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self):
        pass


string = GuitarString()
guitar = Guitar(string)
print(string)
# OUTPUT: <__main__.GuitarString object at 0x7f17531ab160>
print(guitar)  # If I destroy this Guitar instance, the Guitar instance still exists.


# OUTPUT: <__main__.Guitar object at 0x7f17531ab190>


# #3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static


class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add_nums(addition1, addition2, addition3):
        return addition1 + addition2 + addition3


print(Calc.add_nums(3, 4, 3))

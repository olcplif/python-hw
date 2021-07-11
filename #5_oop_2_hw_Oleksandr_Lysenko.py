import dataclasses
from collections import namedtuple


# 1. Make the class with composition.
class Laptop:
    def __init__(self):
        battery1 = Battery(10000)
        self.battery = [battery1]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


hp = Laptop()
print(hp)
# OUTPUT: <__main__.Laptop object at 0x7f4aad1b4070>
print(hp.battery)
# OUTPUT: [<__main__.Battery object at 0x7f1612fe57f0>]


# 2. Make the class with aggregation
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


string = GuitarString()
guitar = Guitar(string)
print(string)
# OUTPUT: <__main__.GuitarString object at 0x7f17531ab160>
print(guitar)  # If I destroy this Guitar instance, the Guitar instance still exists.
# OUTPUT: <__main__.Guitar object at 0x7f17531ab190>


# 3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
class Calc:

    @staticmethod
    def add_nums(addition1, addition2, addition3):
        return addition1 + addition2 + addition3


print(Calc.add_nums(3, 4, 3))
# OUTPUT: 10


# 3. Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


print(Pasta.carbonara())
# OUTPUT: <__main__.Pasta object at 0x7ffa617e94c0>
print(Pasta.bolognaise())
# OUTPUT: <__main__.Pasta object at 0x7ffa617e94c0>


# 5. Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self.visitors = 0

    @property
    def visitors_count(self):
        return self.visitors

    @visitors_count.setter
    def visitors_count(self, count):
        self.visitors = Concert.max_visitors_num if count > Concert.max_visitors_num else count


Concert.max_visitors_num = 100
concert = Concert()
concert.visitors_count = 99
print(concert.visitors_count)
# OUTPUT: 99


# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
# birthday (str), age (int)
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book1 = AddressBookDataClass(1, 'Robert', '911-911-911', 'NY city', 'robert@mail.com', '01/01/1900', 21)
print(address_book1)
# OUTPUT: AddressBookDataClass(key=1, name='Robert', phone_number='911-911-911', address='NY city',
# email='robert@mail.com', birthday='01/01/1900', age=21)
print(address_book1.name)
# OUTPUT: Robert


# 7. Create the same class (6) but using NamedTuple
AddressBookNamedTuple = namedtuple('AddressBookNamedTuple', ['key', 'name', 'phone_number', 'address', 'email',
                                                             'birthday', 'age'])

address_book2 = AddressBookNamedTuple(1, 'Robert', '911-911-911', 'NY city', 'robert@mail.com', '01/01/1900', 21)
print(address_book2)
# OUTPUT: AddressBookNamedTuple(key=1, name='Robert', phone_number='911-911-911', address='NY city',
# email='robert@mail.com', birthday='01/01/1900', age=21)
print(address_book2.email)
# OUTPUT: robert@mail.com


# 8.  Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
class AddressBook:
    __slots__ = ('key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age')

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address_book3 = AddressBook(1, 'Robert Branson', '911-911-911', 'NY city', 'robert@mail.com', '01/01/1900', 21)
print(address_book3.__str__())




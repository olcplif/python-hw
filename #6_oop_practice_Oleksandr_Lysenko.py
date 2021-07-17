from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, total_pests):
        self.vegetables = vegetables
        self.fruits = fruits
        self.total_pests = total_pests

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]
        self.number_of_tomatoes = number_of_tomatoes

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    # HW: get number of tomatoes by property
    @property
    def number_of_fruits(self):
        return self.number_of_tomatoes

    @number_of_fruits.setter
    def number_of_fruits(self, new):
        self.number_of_tomatoes = new

    # HW: destroy tomatoes by pests
    def destroyed(self, other):
        if self.number_of_fruits >= other:
            self.number_of_fruits = self.number_of_fruits - other
        else:
            self.number_of_fruits = 0

    # HW: get state tomatoes -> needs refactoring
    def get_state_fruits(self):
        for tomato in self.tomatoes:
            tomato.states
        return tomato.states


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]
        self.number_of_apples = number_of_apples

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    # HW: get number of apples by property
    @property
    def number_of_fruits(self):
        return self.number_of_apples

    @number_of_fruits.setter
    def number_of_fruits(self, new):
        self.number_of_apples = new

    # HW: destroy tomatoes by pests
    def destroyed(self, other):
        if self.number_of_fruits >= other:
            self.number_of_fruits = self.number_of_fruits - other
        else:
            self.number_of_fruits = 0

    # HW: get state tomatoes -> need refactoring
    def get_state_fruits(self):
        for apple in self.apples:
            apple.states
        return apple.states


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        print(f'{self.name} begins work:')
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    # HW: poisons the pests
    def poison(self):
        if Pests.total_pests != 0:
            print(f'{self.name} poisons the pests!')
            Pests.destroyed_pests()


# HW: Pests
class Pests:
    total_pests = 0
    all_pests = []

    def __init__(self, type_pests, quantity_pests, plants):
        self.type_pests = type_pests
        self.quantity_pests = quantity_pests
        self.plants = plants
        Pests.total_pests += self.quantity_pests
        self.all_pests.append(self)
        # only live pests can eat
        self.live = True

    def eat_the_plants(self):
        if self.live:
            if self.plants.number_of_fruits > 0:
                if self.plants.get_state_fruits() == 2 or self.plants.get_state_fruits() == 3:
                    print(f'Pests attack! {self.quantity_pests} fruit was (were) destroyed!')
                    return self.plants.destroyed(self.quantity_pests)
                else:
                    return print(f'{self.type_pests}s says: "It is not tasty!"')
            else:
                return print(f'{self.type_pests}s says: "No fruit left!"')
        else:
            print('All pests are not alive!')

    # HW: get number of pests by property
    @property
    def number_of_pests(self):
        return self.quantity_pests

    @number_of_pests.setter
    def number_of_pests(self, new):
        self.quantity_pests = new

    # destroy pests by gardener
    @classmethod
    def destroyed_pests(cls):
        for i in range(len(cls.all_pests)):
            cls.all_pests[i].live = False
        cls.total_pests = 0


tomato1 = TomatoBush(6)
apple_tree1 = AppleTree(10)
bugs1 = Pests('Bug', 3, tomato1)
worms1 = Pests('Worm', 4, apple_tree1)
John = Gardener('John', [tomato1, apple_tree1])
garden1 = Garden(tomato1, apple_tree1, Pests.total_pests)

print(f'{tomato1.get_state_fruits()} - current state of tomatoes')
print(f'{Pests.total_pests} - total pests in the garden')
bugs1.eat_the_plants()

John.work()
print(f'{tomato1.get_state_fruits()} - current state of tomatoes')
John.work()
John.work()

worms1.eat_the_plants()
John.poison()
print(f'{tomato1.get_state_fruits()} - current state of tomatoes')
print(f'{tomato1.number_of_tomatoes} tomatoes left')
print(f'{tomato1.number_of_fruits} fruits left')
worms1.eat_the_plants()
print(f'{tomato1.number_of_fruits} fruits left')
worms1.eat_the_plants()
print(f'{tomato1.number_of_fruits} fruits left')
worms1.eat_the_plants()
print(f'{tomato1.number_of_fruits} fruits left')
print(f'{Pests.total_pests} - total pests in the garden')

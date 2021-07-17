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
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')
        print(f'I have such pests {self.pests}')
        print(f'I have such gardener {self.gardener}')


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

    def opportunity_to_be_eaten(self):
        if self.states == 2 or self.states == 3:
            return True
        return False

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

    def opportunity_to_be_eaten(self):
        if self.states == 2 or self.states == 3:
            return True
        return False

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

    # destroyed by pests
    def destroyed(self, other):
        for tomato in self.tomatoes:
            if tomato.opportunity_to_be_eaten():
                return self.number_of_fruits(other)

    @property
    def number_of_fruits(self):
        return self.number_of_tomatoes

    @number_of_fruits.setter
    def number_of_fruits(self, other):
        return len(self.number_of_tomatoes) - other


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def destroyed(self):
        for apple in self.tomatoes:
            if apple.opportunity_to_be_eaten() == True:
                return self.number_of_apples


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')


class Pests:

    def __init__(self, type_pests, quantity_pests, plants):
        self.type_pests = type_pests
        self.quantity_pests = quantity_pests
        self.plants = plants

    @property
    def eat_the_plants(self):
        print('Hrum-hrum')
        if self.plants.destroyed(self.quantity_pests) >= 0:
            return self.plants.destroyed(self.quantity_pests)
            #print(f'{self.quantity_pests} fruits successfully destroyed!'
            #     f'\nThere are {self.plants.destroyed(self.quantity_pests)} fruits left')
        else:
            print(f'All {self.plants}s successfully destroyed!')
            return self.plants.give_away_all()



    #def get_quantity_pests(self):
        #return self.quantity_pests


tomato_bush1 = TomatoBush(6)
apple_tree1 = AppleTree(10)
John = Gardener('John', [tomato_bush1, apple_tree1])
worms1 = Pests('worm', 3, tomato_bush1)
garden1 = Garden(tomato_bush1, apple_tree1, worms1, John)

John.work()
John.work()
John.work()
print(f'{tomato_bush1.number_of_fruits} tomatoes growing in the garden')
# print(f'{tomato_bush1.number_of_tomatoes_on_the_bush - worms1.quantity_pests} tomatoes growing in the garden')

print('Before the invasion pests')
print(f'{worms1.quantity_pests} {worms1.type_pests}s settled in the garden')
worms1.eat_the_plants
print('After the invasion pests')
print(f'{tomato_bush1.number_of_fruits} tomatoes growing in the garden')
# print(garden1.show_the_garden())
John.work()
John.harvest()

# print(tomato_bush1.tomatoes)
# print(apple_tree1.apples)

from __future__ import annotations

from datetime import time

from typing import Dict, Any, Union

import random

from abc import ABC, abstractmethod

import uuid


class Animal(ABC):

    def __init__(self, strength: int, speed: int, name: str):
        self.id = uuid.uuid1()
        self.max_strength = strength
        self.current_strength = strength
        self.speed = speed
        #self.name = name

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):

    def eat(self, forest: Forest):
        # randomly chooses an animal from the forest
        victim_id = random.choice(list(forest.animals.keys()))
        if victim_id == self.id:
            print(f'{self.name} is unlucky - today it will be left without dinner!')
        else:
            print(f'The {self.name} saw and chased the {forest.animals[victim_id].name}!')
            print('...')
            if self.speed >= forest.animals[victim_id].speed:
                print(f'{self.name} caught up the {forest.animals[victim_id].name}!')
                if self.current_strength > forest.animals[victim_id].current_streangth:
                    print(f'{self.name} killed his victim {forest.animals[victim_id].name}!')
                    forest.remove_animal(forest.animals[victim_id])
                    self.revival(50)
                    print(f'Current strength of winner {self.name} = {self.current_strength}')
                else:
                    self.revers_revival(30)
                    print(f'The predator {self.name} could not kill its victim... '
                          f'Its current strength = {self.current_strength}')
                    forest.animals[victim_id].revers_revival(30)
                    print(f'Current strength of victim {forest.animals[victim_id].name} = '
                          f'{forest.animals[victim_id].current_strength}')
            else:
                self.revers_revival(30)
                print(f'The predator {self.name} did not catch up the {forest.animals[victim_id].name}... '
                      f'Its current strength = {self.current_strength}')
                forest.animals[victim_id].revers_revival(30)
                print(f'Current strength of lucky victim {forest.animals[victim_id].name} = '
                      f'{forest.animals[victim_id].current_strength}')

        if victim_id in forest.animals.keys():
            if forest.animals[victim_id].current_strength <= 0:
                print(f'The {forest.animals[victim_id].name} died...')
                forest.remove_animal(forest.animals[victim_id])

        if self.current_strength <= 0:
            print(f'The {self.name} died...')
            forest.remove_animal(self)

    def revival(self, num):
        per_cent = num / 100
        if (self.current_strength + (self.current_strength * per_cent)) <= self.max_strength:
            self.current_strength = self.current_strength * per_cent + self.current_strength
        else:
            self.current_strength = self.max_strength
            print(f'{self.name} recovered strength to {self.current_strength}')

    def revers_revival(self, num):
        per_cent = num / 100
        self.current_strength = self.current_strength - self.current_strength * per_cent
        print(f'{self.name} lost strength to {self.current_strength}')


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        # restores its strength by 50%
        self.revival(50)

    def revival(self, num):
        per_cent = num / 100
        if (self.current_strength + self.current_strength * per_cent) <= self.max_strength:
            self.current_strength = self.current_strength * per_cent + self.current_strength
        else:
            self.current_strength = self.max_strength
        print(f'{self.name} recovered strength to {self.current_strength}')

    def revers_revival(self, num):
        per_cent = num / 100
        self.current_strength = self.current_strength - self.current_strength * per_cent
        print(f'{self.name} lost strength to {self.current_strength}')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(animal.id)

    def any_predator_left(self):
        flag = False
        for key in self.animals:
            if isinstance(self.animals[key], Predator):
                flag = True
        return flag


def animal_generator():
    # animal_generator to create a random animal
    names_predator = ['lion', 'wolf', 'fox']
    names_herbivorous = ['deer', 'antelope', 'rabbit']
    types_animal = ['Herbivorous', 'Predator']
    nature_ = []
    type_animal = random.choice(types_animal)
    if type_animal == 'Herbivorous':
        nature_.append(Herbivorous(random.randrange(25, 100, 1), random.randrange(25, 100, 1),
                                   random.choice(names_herbivorous)))
    else:
        nature_.append(Predator(random.randrange(25, 100, 1), random.randrange(25, 100, 1),
                                random.choice(names_predator)))
    yield nature_


if __name__ == "__main__":
    nature = animal_generator()
    nature_iterator = iter(nature)
    forest = Forest()

    for i in range(5):
        animal = next(nature_iterator)
        forest.add_animal(animal)

    while True:
        if not forest.any_predator_left():
            break
        for animal in forest:
            animal.eat(forest=forest)
        time.sleep(1)

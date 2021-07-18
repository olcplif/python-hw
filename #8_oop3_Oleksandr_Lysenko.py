from __future__ import annotations

from typing import Dict, Any


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        pass

    def check_strength(self):
        pass


class Predator:

    def eat(self, forest: Forest):
        pass

    def hunts(self, forest: Forest, animal: AnyAnimal):
        # randomly chooses an animal from the forest
        pass


class Herbivorous:

    def eat(self, forest: Forest):
        pass


AnyAnimal = Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    pass


if __name__ == "__main__":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass

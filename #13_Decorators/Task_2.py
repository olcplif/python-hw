# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор
# на функцію,який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід
# на екран наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.


def print_hypotenuse(func):
    def wrap(leg_1, leg_2):
        result = func(leg_1, leg_2)
        print(f"At legs {leg_1} and {leg_2} the hypotenuse is equal to {result}")
        return result

    return wrap


@print_hypotenuse
def get_hypotenuse(leg_1, leg_2):
    hypotenuse = (((leg_1 ** 2) + (leg_2 ** 2)) ** 0.5)
    return hypotenuse


get_hypotenuse(3, 4)

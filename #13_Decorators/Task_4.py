# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних


def convert_to_str(func):
    def wrap(*args, **kwargs):
        return [str(el) for el in func(*args, **kwargs)]

    return wrap


@convert_to_str
def create_list(n):
    return [el for el in range(n + 1)]


print(create_list(7))

# ['0', '1', '2', '3', '4', '5', '6', '7']

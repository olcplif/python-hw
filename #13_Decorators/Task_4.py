# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних


def convert_to_str(func):
    def wrap(n):
        str_list = [str(el) for el in func(n)]
        return str_list

    return wrap


@convert_to_str
def create_list(n):
    list_ = [el for el in range(n + 1)]
    return list_


print(create_list(7))

# ['0', '1', '2', '3', '4', '5', '6', '7']

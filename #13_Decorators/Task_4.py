# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних


def convert_to_str(func):
    def wrap(n):
        str_list = []
        for el in func(n):
            el = str(el)
            str_list.append(el)
        return str_list

    return wrap


@convert_to_str
def create_list(n):
    list_ = []
    for el in range(n + 1):
        list_.append(el)
    return list_


print(create_list(7))

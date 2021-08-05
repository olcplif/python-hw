# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
import time


def check_time(func):
    def wrap(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        print(f">> This function was performed for {time.time() - time_start} seconds. <<")
        return result

    return wrap


@check_time
def create_list():
    print('Enter "stop" for exit.')
    list_var = []
    while True:
        var = input('Enter data: ')
        if var == 'stop':
            break
        list_var.append(var)
    return list_var


print(create_list())

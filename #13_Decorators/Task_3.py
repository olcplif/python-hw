# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор
# який перед тим як запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка,
# яку можна перевести в число, (наприклад “1”) то строка приводиться до чисельного типу даних


def check_data(func):
    def wrap(list_):
        def check_convert_to_float(el_):
            try:
                float(el_)
                return True
            except ValueError:
                return False
        filter_list = []
        for el in list_:
            check_int = isinstance(el, int)
            check_float = isinstance(el, float)
            check_convert_to_int = str(el).isdigit()
            if check_int or check_float:
                filter_list.append(el)
            elif check_convert_to_int:
                convert_el = int(el)
                filter_list.append(convert_el)
            elif check_convert_to_float(el):
                convert_el = float(el)
                filter_list.append(convert_el)
        result = func(filter_list)
        print(list_)
        print(filter_list)
        print(f"The sum of the items in the filtered list =  {result}")
        return result

    return wrap


@check_data
def sum_list(list_):
    sum_el = sum(list_)
    return sum_el


sum_list([1, '6', 2.0, 't', '4r', '4.5'])

# 1. Дану задачу робити через декоратор як функції!
# Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
# Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
# Приклад:
# @decor(int, float, int, float)
# def func(1, 1.2, 4)
# Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
# функція повертає
# можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується
#
#
# 2. Те ж саме що й в завданні 1, але зробити через функтор


class WrongType(Exception):
    pass


class WrongTypeResult(WrongType):
    pass


class WrongNumArgs(Exception):
    pass


class CheckArgumentTypes:
    def __init__(self, *filter_types):
        self.filter_types = filter_types

    def __call__(self, func):
        def wrap(*args_func):
            try:
                if len(self.filter_types) != len(args_func) + 1:
                    raise WrongNumArgs
                else:
                    for i in range(len(args_func)):
                        if type(args_func[i]) != self.filter_types[i]:
                            raise WrongType
                    if type(func(*args_func)) != self.filter_types[-1]:
                        raise WrongTypeResult
                    else:
                        return func(*args_func)

            except WrongTypeResult:
                return "Argument-result type do not match the decorator"
            except WrongType:
                return "Argument types do not match the decorator"
            except WrongNumArgs:
                return "Error numbers of arguments"

        return wrap


@CheckArgumentTypes(int, float, int, float)
def func_sum(a, b, c):
    return sum([a, b, c])


print(func_sum(2, 2.2, 2))

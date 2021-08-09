# 1. Дану задачу робити через декоратор як функції!
# Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
# Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
# Приклад:
# @decor(int, float, int, float)
# def func(1, 1.2, 4)
# Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
# функція повертає
# можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується

class WrongType(Exception):
    pass


class WrongTypeResult(WrongType):
    pass


class WrongNumArgs(Exception):
    pass


def check_argument_types(*args_decor):
    def wrap(func):
        def check(*args_func):
            try:
                if len(args_decor) != len(args_func) + 1:
                    raise WrongNumArgs
                else:
                    for i in range(len(args_func)):
                        if type(args_func[i]) != args_decor[i]:
                            raise WrongType
                    if type(func(*args_func)) != args_decor[-1]:
                        raise WrongTypeResult
                    else:
                        return func(*args_func)

            except WrongTypeResult:
                return "Argument-result type do not match the decorator"
            except WrongType:
                return "Argument types do not match the decorator"
            except WrongNumArgs:
                return "Error numbers of arguments"

        return check

    return wrap


@check_argument_types(int, float, int, float)
def func_sum(a, b, c):
    return sum([a, b, c])


print(func_sum(1, 1.1, 1))



class Calc:
    @staticmethod
    def sum(a: int, b: int) -> int:
        """ Шукає суму двох чисел
        >>> Calc.sum(4, 5)
        9

        Використовуючи формулу a + b
        :param a: перший доданок, може бути int або float
        :param b: другий доданок, може бути int або float
        :return: сума доданків, може бути int або float залежно від параметрів
        """
        return a + b

    @staticmethod
    def minus(a: int, b: int) -> int:
        """ Шукає різницю двох чисел
        >>> Calc.minus(5, 4)
        1

        Використовуючи формулу a - b
        :param a: перший від'ємник, може бути int або float
        :param b: другий від'ємник, може бути int або float
        :return: різниця від'ємників, може бути int або float залежно від параметрів
        """
        return a - b

    @staticmethod
    def mul(a: int, b: int) -> int:
        """ Шукає добуток двох чисел
        >>> Calc.mul(3, -4)
        -12

        Використовуючи формулу a * b
        :param a: множене, може бути int або float
        :param b: множник, може бути int або float
        :return: добуток, може бути int або float залежно від параметрів
        """
        return a * b

    @staticmethod
    def div(a: int, b: int) -> float:
        """ Шукає частку двох чисел
        >>> Calc.div(-4, -2)
        2.0

        Використовуючи формулу a / b
        :param a: ділене, може бути int або float
        :param b: дільник, може бути int або float
        :return: частка, може бути тільки float
        """
        return a / b

    @staticmethod
    def percent(a: int, b: int) -> float:
        """ Шукає процент від числа
        >>> Calc.percent(20, 50)
        10.0

        Використовуючи формулу a / 100 * b
        :param a: число, з якого визначається відсоток, може бути int або float
        :param b: шуканий відсоток, може бути int або float
        :return: відсоток від числа, може бути тільки float
        """
        return a / 100 * b

    @staticmethod
    def pow(a: int, b: int) -> int:
        """ Шукає степінь числа
        >>> Calc.pow(3, 2)
        9

        Використовуючи формулу a ** b
        :param a: число, яке підноситься до степеню, може бути int або float
        :param b: степінь, може бути int або float
        :return: число піднесене до степеня, може бути int або float
        """
        return a ** b

    @staticmethod
    def root(a: int, b=2) -> float:
        """ Шукає корінь числа
        >>> Calc.root(9, 2)
        3.0

        Використовуючи формулу a ** (1 / b)
        :param a: число, з якого шукається корінь, може бути int або float
        :param b: степінь кореня (по замовчуванню - квадратний корінь), може бути int
        :return: корінь числа, може бути тільки float
        """
        return a ** (1 / b)

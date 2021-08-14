# 1. Написати програму яка буде обраховувати два квадратних рівняня одночасно, всі параметри рівняння задати в змінні.

from threading import Thread
import random
import time
import logging

_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=_format, level=logging.INFO, datefmt="%H:%M:%S")


class ErrorValidQuadratic(Exception):
    pass


class ErrorValidRoots(Exception):
    pass


# (a * (x ** 2)) + (b * x) + c == 0
# a != 0
class QuadraticEquation(Thread):
    def __init__(self, a, b, c, name):
        Thread.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.name = name

    def run(self):
        logging.info(f"INFO:    Created equation with such coefficients ({self.a}, {self.b}, {self.c})")
        delay = random.randint(1, 3)
        time.sleep(delay)
        logging.info(f"INFO:    {self.name} is starting")
        try:
            if self.a == 0:
                raise ErrorValidQuadratic
            else:
                d = self.b ** 2 - 4 * self.a * self.c
                if d > 0:
                    x1 = (-self.b + ((self.b ** 2 - 4 * self.a * self.c) ** 0.5)) / (2 * self.a)
                    x2 = (-self.b - ((self.b ** 2 - 4 * self.a * self.c) ** 0.5)) / (2 * self.a)
                    result = (x1, x2)
                    logging.info(
                        f"INFO:    Solution of the equation with such coefficients "
                        f"({self.a}, {self.b}, {self.c}) is {result}")
                    return result
                elif d == 0:
                    x = -self.b / (2 * self.a)
                    result = x
                    logging.info(
                        f"INFO:    Solution of the equation with such coefficients "
                        f"({self.a}, {self.b}, {self.c}) is {result}")
                    return result
                else:
                    raise ErrorValidRoots

        except ErrorValidQuadratic:
            logging.warning(
                f"WARNING: Equation with such coefficients ({self.a}, {self.b}, {self.c}) isn't quadratic")
            return f"Equation with such coefficients ({self.a}, {self.b}, {self.c}) isn't quadratic"
        except ErrorValidRoots:
            logging.warning(
                f"WARNING: Equation with such coefficients ({self.a}, {self.b}, {self.c}) hasn't valid roots")
            return f"Equation with such coefficients ({self.a}, {self.b}, {self.c}) hasn't valid roots"
        finally:
            logging.info(f"INFO:    {self.name} is finishing")


def create_treads():
    for i in range(5):
        name = f"Thread #{i + 1}"
        # Create equation with random coefficients
        my_thread = QuadraticEquation(random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3), name)
        my_thread.start()


create_treads()

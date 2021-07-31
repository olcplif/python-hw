import logging

template_log = "%(asctime)s - %(levelname)s: %(message)s"
file_log = "calc_log.log"

logging.basicConfig(filename=file_log, filemode='a', level=logging.INFO, format=template_log)


class OpenLogFile:
    def __init__(self, path, access_attr='a'):
        self.file = open(path, access_attr)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            logging.info('Log-file closed!')
            self.file.close()
        elif exc_type is Exception:
            print(exc_type, exc_val, exc_tb)
            return True


with open('calc_log.log', 'a') as file:
    logging.info(f'Log file <{file}> opened.')


class Calc:
    calc_commands = ['+', '-', '*', '/', '**', 'root', '%']

    def __init__(self):
        pass

    @staticmethod
    def solution(_operand_1, _operand_2, comm):
        if Command.get_command(comm) == '+':
            result = Operand.__add__(_operand_1, _operand_2)
        elif Command.get_command(comm) == '-':
            result = Operand.__sub__(_operand_1, _operand_2)
        elif Command.get_command(comm) == '*':
            result = Operand.__mul__(_operand_1, _operand_2)
        elif Command.get_command(comm) == '/':
            result = Operand.__truediv__(_operand_1, _operand_2)
        elif Command.get_command(comm) == '**':
            result = Operand.__pow__(_operand_1, _operand_2)
        elif Command.get_command(comm) == 'root':
            result = Operand.root(_operand_1, _operand_2)
        elif Command.get_command(comm) == '%':
            result = Operand.percent(_operand_1, _operand_2)

        logging.info(f'{Operand.get_operand(_operand_1)} {Command.get_command(comm)} '
                     f'{Operand.get_operand(_operand_2)} = {result}')
        return print(f'{Operand.get_operand(_operand_1)} {Command.get_command(comm)} '
                     f'{Operand.get_operand(_operand_2)} = {result}')

    @staticmethod
    def check_stop(str_):
        if str_.lower() == 'stop':
            logging.info('*** Program exit ***')
            raise SystemExit


class Operand(Calc):
    def __init__(self, number_of_operand):
        self.number_of_operand = number_of_operand
        super().__init__()

    @staticmethod
    def is_integer(num):
        try:
            float(num)
        except ValueError:
            return False
        else:
            return float(num).is_integer()

    def check_operand(self):
        while True:
            try:
                var = input(f'Enter {self.number_of_operand}: ')
                Calc.check_stop(var)
                if float(var) or float(var) == 0.0:
                    if float(var) == 0.0:
                        logging.info(f"---> Dirty hack is present in the definition of {self.number_of_operand}! "
                                     f"Because float('0') != True")
                    if self.is_integer(var):
                        try:
                            operand = int(var)
                            logging.info(f'{self.number_of_operand} = {var} is type integer')
                        except ValueError:
                            operand = float(var)
                    else:
                        operand = float(var)
                        logging.info(f'{self.number_of_operand} = {var} is type float')
                    return operand
            except (ValueError, TypeError):
                print('---> Enter the correct type: int or float!')
                logging.error(f"---> {self.number_of_operand} = <{var}> isn't correct  number")

    def get_operand(self):
        return self

    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other

    def __mul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            result = self / other
        except ZeroDivisionError:
            logging.warning('---> Warning! Division by zero!')
            result = 0
        return result

    def __pow__(self, other):
        return self ** other

    @staticmethod
    def root(self, other):
        try:
            result = pow(self, (1 / other))
        except ZeroDivisionError:
            logging.warning('---> Warning! Division by zero:')
            result = 0
        return result

    @staticmethod
    def percent(self, other):
        return self / 100 * other


class Command(Calc):
    def __init__(self):
        super().__init__()

    @staticmethod
    def check_command():
        while True:
            try:
                comm = input('Enter command: ')
                Calc.check_stop(comm)
                if comm in Calc.calc_commands:
                    logging.info(f'selected command -> "{comm}"')
                    return comm
                else:
                    raise ValueError
            except ValueError:
                print(f'---> Enter the correct command! {Calc.calc_commands}')
                logging.error(f"---> <'{comm}'> isn't correct command!")

    def get_command(self):
        return self


print('*' * 30)
print("Enter 'stop' for exit!")
print('*' * 30)

while True:
    operand_1 = Operand('operand1').check_operand()
    command = Command().check_command()
    operand_2 = Operand('operand2').check_operand()
    Calc().solution(operand_1, operand_2, command)
    print('*' * 30)

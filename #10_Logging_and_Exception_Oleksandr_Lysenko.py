calc_commands = ['+', '-', '*', '/', '**', 'pow', '%']

while True:
    flag = True
    while flag:
        try:
            operand_1 = int(input('Enter operand1:'))
        except ValueError:
            print('--- Enter the correct number!')
            flag = True
        except TypeError:
            print('--- Use the correct type for number!')
            flag = True
        else:
            flag = False

    flag = True
    while flag:
        command = input('Enter command:')
        if command in calc_commands:
            flag = False
        else:
            print('--- Enter the correct command!')
            flag = True

    flag = True
    while flag:
        try:
            operand_2 = int(input('Enter operand2:'))
        except ValueError:
            print('--- Enter the correct number!')
            flag = True
        else:
            flag = False

    if command == '+':
        solution = operand_1 + operand_2
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == '-':
        solution = operand_1 - operand_2
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == '*':
        solution = operand_1 - operand_2
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == '/':
        try:
            solution = operand_1 / operand_2
        except ZeroDivisionError:
            print('--- Warning! Division by zero:')
            solution = 0
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == '**':
        solution = operand_1 ** operand_2
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == 'pow':
        solution = pow(operand_1, (1 / operand_2))
        print(f'{operand_1} {command} {operand_2} = {solution}')
    elif command == '%':
        solution = operand_1 / 100 * operand_2
        print(f'{operand_2} percent of the number {operand_1} = {solution}')

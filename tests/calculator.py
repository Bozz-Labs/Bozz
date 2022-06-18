def calculator():
    math_type = input('Welcome to the calculator! Choose: +, -, *, / ')
    if math_type == '+':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number + second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            exit()
    elif math_type == '-':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number - second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            exit()
    elif math_type == '*':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number * second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            exit()
    elif math_type == '/':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number / second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            exit()

calculator()
def welcome():
    print('Welcome to Calculator')
welcome()

def calculate():
    num_1 = int(input('Please enter the first number: '))
    operation = input('Please type in the math operation you would like to complete:(+ ,- , * , / )')
    num_2 = int(input('Please enter the second number: '))
    

    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
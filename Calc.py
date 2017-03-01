
""" Use give operator * / + -, to exit use 'q' """
# Get input
# Check how correct are the inputs
# Get input from file
OPERATOR_LIST = ["-", "+", "*", "/", "l", "q"]

log = open('calc_log.txt', 'r')

def check_operator():

    while True:
        print('What would you like to do')

        operator = input('( -, +, *, /, l, q) operator?')

        if operator not in OPERATOR_LIST:
            print("not valid operator")
            continue
        # elif operator == OPERATOR_LIST[4]:
        #     return operator = log.read()
        elif operator == OPERATOR_LIST[5]:
            exit()
        else:
            return operator
        print('Provide values')


def check_input():
    while True:
        values = [input('value_1?\n'), input('value_2?\n')]
        try:
            for i in range(len(values)):
                if values[i] == "_":
                    values[i] = output
                else:
                    values[i] = int(values[i])
        except ValueError as e:
            print(e)
            continue
        else:
            print('OK')
            return values

def make_calc(operator, values):

    if operator == OPERATOR_LIST[4]:
        log = open('calc_log.txt', 'r')
        lines = log.readlines()
        line = 0
        operator = lines[line].split(' ')[0]
        values = int(lines[line].split(' ')[1]), int(lines[line].split(' ')[2]),

    if operator == OPERATOR_LIST[0]:
        output = values[0] - values[1]
    elif operator == OPERATOR_LIST[1]:
        output = values[0] + values[1]
    elif operator == OPERATOR_LIST[2]:
        output = values[0] * values[1]
    elif operator == OPERATOR_LIST[3]:
        try:
            output = values[0] / values[1]
        except ZeroDivisionError as e:
            print("Can't divide by 0")
    log = open('calc_log.txt', 'a')
    log.write('{} {} {} \n'.format(operator, values[0], values[1]))
    print(output)
    return output


while True:
    output = make_calc(check_operator(), check_input())

x = log.read()
print(x)

log.close()

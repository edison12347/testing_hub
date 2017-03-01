
""" Use give operator * / + -, to exit use 'q' """
# Get input
# Check how correct are the inputs
# Get input from file
SUM = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"
QUIT = "q"
LOAD = "l"
OPERATOR_LIST = [SUM, MINUS, MULTIPLY, DIVIDE, LOAD, QUIT]


def get_input():

    while True:
        print('What would you like to do')

        operator = input('( -, +, *, /, l, q) operator?')

        if operator not in OPERATOR_LIST:
            print("not valid operator")
            continue

        elif operator == QUIT:
            exit()
        break
    if operator == LOAD:
        return [None, None], operator

    while True:
        print('Provide values')
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
        return values, operator


def load_log(line):
    log = open('calc_log.txt', 'r')
    lines = log.readlines()
    split_results = lines[line].split(' ')
    operator = split_results[0]
    values = int(split_results[1]), int(split_results[2]),
    return values, operator


def make_operation(values, operator):
    if operator == SUM:
        output = values[0] + values[1]
    elif operator == MINUS:
        output = values[0] - values[1]
    elif operator == MULTIPLY:
        output = values[0] * values[1]
    elif operator == DIVIDE:
        try:
            output = values[0] / values[1]
        except ZeroDivisionError as e:
            print("Can't divide by 0")
    return output

def make_calc(values, operator):
    if operator == LOAD:
        log = open('calc_log.txt', 'r')
        for line in range(len(log.readlines())):
            values, operator = load_log(line)
            output = make_operation(values, operator)
            print("line: ",line, ' output: ',output)
        return output

    output = make_operation(values, operator)
    log = open('calc_log.txt', 'a')
    log.write('{} {} {} \n'.format(operator, values[0], values[1]))
    print('Result: ', output)
    return output


while True:
    values, operator = get_input()
    output = make_calc(values, operator)

log.close()

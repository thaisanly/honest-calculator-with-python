# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

messages = {
    "msg_10": msg_10,
    "msg_11": msg_11,
    "msg_12": msg_12,
}

memory = 0
operators = ["+", "-", "*", "/"]
yes_no = ['y', 'n']


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def parse_number(string):
    if is_float(string):
        return float(string)

    if string.isnumeric():
        return int(string)

    return None


def parse_calculation(text):
    global memory

    split = text.split(' ')

    if len(split) != 3:
        return {"x": None, 'operator': None, "y": None}

    _x = parse_number(split[0])
    _operator = split[1]
    _y = parse_number(split[2])

    if split[0] == 'M':
        _x = float(memory)

    if split[2] == 'M':
        _y = float(memory)

    return {"x": _x, 'operator': _operator, "y": _y}


def is_valid_operand(parsed):
    return parsed.get('x') is not None and parsed.get('y') is not None


def is_valid_operator(parsed):
    return parsed.get('operator') in operators


def is_valid_division(parsed):
    if parsed.get('operator') != '/':
        return True

    return parsed.get('y') != 0


def is_valid_input(parsed):
    return (is_valid_operand(parsed) and
            is_valid_operator(parsed) and
            is_valid_division(parsed))


def calculate(parsed):
    if parsed.get('operator') == '+':
        return parsed.get("x") + parsed.get('y')

    if parsed.get('operator') == '-':
        return parsed.get("x") - parsed.get('y')

    if parsed.get('operator') == '*':
        return parsed.get("x") * parsed.get('y')

    if parsed.get('operator') == '/':
        return parsed.get("x") / parsed.get('y')

    return None


def is_one_digit(num):
    if num.is_integer() and (10 > num > -10):
        return True
    else:
        return False


def validate_input(parsed):
    msg = ""

    x = parsed.get('x')
    y = parsed.get('y')
    opt = parsed.get('operator')

    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6

    if (x == 1 or y == 1) and opt == "*":
        msg = msg + msg_7

    if (x == 0 or y == 0) and opt in ['*', '+', '-']:
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


def parse_user_input():
    print(msg_0)
    parsed = parse_calculation(input())
    validate_input(parsed)

    while not is_valid_input(parsed):

        if not is_valid_operand(parsed):
            print(msg_1)
            print(msg_0)
            parsed = parse_calculation(input())
            validate_input(parsed)

            continue

        if not is_valid_operator(parsed):
            print(msg_2)
            print(msg_0)
            parsed = parse_calculation(input())
            validate_input(parsed)
            continue

        if not is_valid_division(parsed):
            print(msg_3)
            print(msg_0)
            parsed = parse_calculation(input())
            validate_input(parsed)
            continue

    return parsed


def confirmed_store_single_digit():
    is_store_one_digit = 'n'

    msg_index = 10

    while msg_index < 12 or is_store_one_digit == 'y':

        # ask if user want to store single digit
        print(messages[f'msg_{msg_index}'])
        is_store_one_digit = input()
        while is_store_one_digit not in yes_no:
            is_store_one_digit = input()

        if is_store_one_digit == 'y' and msg_index < 12:
            msg_index += 1
        else:
            break

    return is_store_one_digit == 'y'


def run_calculator():
    global memory

    parsed = parse_user_input()
    result = calculate(parsed)
    print(result)

    # Do you want to store the result? (y / n):
    print(msg_4)
    is_store_result = input()
    while is_store_result not in yes_no:
        print(msg_4)
        is_store_result = input()

    if is_store_result == 'y' and not is_one_digit(result):
        memory = result

    # Are you sure? It is only one digit! (y / n)
    if is_store_result == 'y' and is_one_digit(result) and confirmed_store_single_digit():
        memory = result

    # Do you want to continue calculations? (y / n):
    print(msg_5)
    is_continuous = input()
    while is_continuous not in yes_no:
        is_continuous = input()

    if is_continuous == 'n':
        exit()

    return run_calculator()


run_calculator()

import sys

factor_converters = {'km': 0.6213712, 'mi': 1.609344}


def converter(number, unit):
    if number < 0:
        return 'Invalid length'
    return f'{number * factor_converters[unit]}'


def is_valid_input(length):
    length_unit = length.split('_')
    return len(length_unit) == 2 and length_unit[1] in factor_converters.keys() or length == 'e'


def get_string(param=''):
    return input(param)


def _exit(param=''):
    sys.exit(param)


def input_process(length):
    if length == 'e':
        _exit()
    if is_valid_input(length):
        return length.split('_')
    return -1, -1


def print_menu():
    print('Unit Converter')
    print('Enter a length as number_mi to convert miles to kilometer')
    print('example: 1_mi')
    print('Enter a length as number_mi to convert miles to kilometer')
    print('example: 1_km')
    print('Enter e to exit\n')


def main():
    print_menu()
    length = get_string('Input : ')
    number, unit = input_process(length)
    result = converter(int(number), unit)
    return result


def run():
    while True:
        print(main())


if __name__ == '__main__':
    run()

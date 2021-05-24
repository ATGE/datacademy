import math
import sys


def get_float(param=''):
    while True:
        try:
            return float(input(param))
        except ValueError:
            print('Invalid number')


def sphere():
    radius = get_float('radius :')
    result = 4 / 3 * math.pi * radius ** 3
    return f'Sphere area : {result}'


def cylinder():
    radius = get_float('height :')
    height = get_float('radius :')
    result = math.pi * height * radius ** 2
    return f'Cylinder area : {result}'


def cone():
    radius = get_float('radius :')
    height = get_float('height :')
    result = 1 / 3 * math.pi * height * radius ** 2
    return f'Cone area : {result}'


def cube():
    length = get_float('length :')
    result = length ** 3
    return f'Cube area : {result}'


def _exit():
    sys.exit('bye')


def print_menu():
    print('Choose an shape')
    print('1: sphere')
    print('2: cylinder')
    print('3: cone')
    print('4: cube')
    print('5: exit')


def main():
    options = {1.0: 'sphere', 2.0: 'cylinder', 3.0: 'cone', 4.0: 'cube', 5.0: '_exit'}
    print_menu()
    option = get_float('input : ')
    if option not in options.keys():
        return 'Invalid option'
    return globals()[options[option]]()


def run():
    while True:
        print(main())


if __name__ == '__main__':
    run()

def get_float(param=''):
    while True:
        try:
            return float(input(param))
        except ValueError:
            print('Invalid number')


def game():
    while True:
        print('Enter tree number:')
        lower_limit = get_float('first number :')
        upper_limit = get_float('second number :')
        comparison = get_float('third number :')
        if lower_limit <= comparison <= upper_limit:
            return f'number {comparison} is in  range'
        return f'number {comparison} is out of range'


if __name__ == '__main__':
    print(game())

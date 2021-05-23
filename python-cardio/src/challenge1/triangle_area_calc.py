def get_float(param=''):
    while True:
        try:
            return float(input(param))
        except ValueError:
            print('Invalid number')


def get_area(base, height):
    return (base * height) / 2


def main():
    base = get_float('base : ')
    height = get_float('height : ')
    area = get_area(base, height)
    return f'Triangle are: {area}'


def run():
    print(run)


if __name__ == '__main__':
    run()

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
PLAYER1 = 'player1'
PLAYER2 = 'player2'
TIE = 'tie'
game_statistics = {PLAYER1: 0, PLAYER2: 0, TIE: 0, 'rounds': 0}
MAX_ROUNDS = 3
valid_inputs = (ROCK, PAPER, SCISSORS)


def is_valid_input(string):
    return string in valid_inputs


def get_string(param=''):
    while True:
        result = input(param)
        if is_valid_input():
            return result
        print('Invalid input')


def get_winner(player1, player2):
    _index = {ROCK: 0, PAPER: 1, SCISSORS: 2}
    # player 2 :rock paper scissors      / player 1:
    _winner = [[TIE, PLAYER2, PLAYER1],  # rock
               [PLAYER1, TIE, PLAYER2],  # paper
               [PLAYER2, PLAYER1, TIE]]  # scissors
    result = _winner[_index[player1]][_index[player2]]
    return result


def print_string(string=''):
    print(string)


def play():
    for _round in range(MAX_ROUNDS):
        result = get_winner(get_string('player 1:'), get_string('player 2:'))
        game_statistics[result] += 1
        if result is TIE:
            print_string('tie')
        else:
            print_string(f'{result} wins')
        if game_statistics[result] > MAX_ROUNDS / 2 and result is not TIE:
            break

    if game_statistics[TIE] == MAX_ROUNDS or game_statistics[PLAYER1] == game_statistics[PLAYER2]:
        return f'{PLAYER1} and {PLAYER2} tied'
    elif game_statistics[PLAYER1] > game_statistics[PLAYER2]:
        return f'game winner {PLAYER1}'
    else:
        return f'game winner {PLAYER2}'


def run():
    print(play())


if __name__ == '__main__':
    play()

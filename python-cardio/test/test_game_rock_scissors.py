import unittest
from unittest import mock

from src.challenge2 import game_rock_paper_scissors as game


class GameRockPaperScissors(unittest.TestCase):
    def setUp(self):
        super(GameRockPaperScissors, self).setUp()
        self.game = game
        self.game_status = self.game.game_statistics.copy()

    def tearDown(self):
        super(GameRockPaperScissors, self).tearDown()
        self.game.game_statistics = self.game_status.copy()

    def test_get_winner_tie_rr(self):
        output = self.game.get_winner(game.ROCK, game.ROCK)
        self.assertEqual(game.TIE, output)

    def test_get_winner_tie_pp(self):
        output = self.game.get_winner(game.PAPER, game.PAPER)
        self.assertEqual(game.TIE, output)

    def test_get_winner_player1_rs(self):
        output = self.game.get_winner(game.ROCK, game.SCISSORS)
        self.assertEqual(game.PLAYER1, output)

    def test_get_winner_player1_pr(self):
        output = self.game.get_winner(game.PAPER, game.ROCK)
        self.assertEqual(game.PLAYER1, output)

    def test_get_winner_player1_sp(self):
        output = self.game.get_winner(game.SCISSORS, game.PAPER)
        self.assertEqual(game.PLAYER1, output)

    def test_get_winner_player2_ps(self):
        output = self.game.get_winner(game.PAPER, game.SCISSORS)
        self.assertEqual(game.PLAYER2, output)

    def test_play_tie_round3(self):
        _side_effect = [game.ROCK, game.ROCK] + [game.ROCK, game.ROCK] + [game.ROCK, game.ROCK]

        with mock.patch('src.challenge2.game_rock_paper_scissors.get_string', side_effect=_side_effect):
            expected_result = f'{game.PLAYER1} and {game.PLAYER2} tied'
            output = self.game.play()
            self.assertEqual(expected_result, output)

    def test_play_player1_win_round3(self):
        _side_effect = [game.ROCK, game.ROCK] + [game.ROCK, game.ROCK] + [game.ROCK, game.SCISSORS]

        with mock.patch('src.challenge2.game_rock_paper_scissors.get_string', side_effect=_side_effect):
            expected_result = f'game winner {game.PLAYER1}'
            output = self.game.play()
            self.assertEqual(expected_result, output)

    def test_play_player1_win_round2(self):
        _side_effect = [game.PAPER, game.ROCK] + [game.SCISSORS, game.PAPER]

        with mock.patch('src.challenge2.game_rock_paper_scissors.get_string', side_effect=_side_effect):
            expected_result = f'game winner {game.PLAYER1}'
            output = self.game.play()
            self.assertEqual(expected_result, output)

    def test_play_player2_win_round3(self):
        _side_effect = [game.ROCK, game.PAPER] + [game.PAPER, game.ROCK] + [game.PAPER, game.SCISSORS]

        with mock.patch('src.challenge2.game_rock_paper_scissors.get_string', side_effect=_side_effect):
            expected_result = f'game winner {game.PLAYER2}'
            output = self.game.play()
            self.assertEqual(expected_result, output)

    def test_play_player2_win_round2(self):
        _side_effect = [game.PAPER, game.SCISSORS] + [game.ROCK, game.PAPER]

        with mock.patch('src.challenge2.game_rock_paper_scissors.get_string', side_effect=_side_effect):
            expected_result = f'game winner {game.PLAYER2}'
            output = self.game.play()
            self.assertEqual(expected_result, output)


if __name__ == '__main__':
    unittest.main()

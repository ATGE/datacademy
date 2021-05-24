import unittest
from unittest import mock

from src.challenge5 import changing_ranges


class ChangingRanges(unittest.TestCase):
    def test_changing_ranges_in(self):
        with mock.patch('src.challenge5.changing_ranges.get_float', side_effect=[1, 2, 1.5]):
            output = changing_ranges.game()
            self.assertEqual(output, 'number 1.5 is in  range')

    def test_changing_ranges_out(self):
        with mock.patch('src.challenge5.changing_ranges.get_float', side_effect=[1, 2, 3]):
            output = changing_ranges.game()
            self.assertEqual(output, 'number 3 is out of range')


if __name__ == '__main__':
    unittest.main()

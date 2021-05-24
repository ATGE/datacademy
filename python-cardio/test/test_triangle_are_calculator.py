import unittest
from unittest import mock

from src.challenge1 import triangle_area_calc as delta


class TriangleArea(unittest.TestCase):
    def test_changing_ranges_in(self):
        input_base_height = [100, 50]
        with mock.patch('src.challenge1.triangle_area_calc.get_float', side_effect=input_base_height):
            expected_output = f'Triangle are: {100 * 50 / 2}'
            output = delta.main()
            self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()

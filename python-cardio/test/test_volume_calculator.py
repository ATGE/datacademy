import unittest
from unittest import mock

from src.challenge4 import volume_calc


class VolumeCalculator(unittest.TestCase):

    def test_is_valid_input_mi(self):
        with mock.patch('src.challenge4.volume_calc.get_float', side_effect=[1, 1]):
            output = volume_calc.main()
            self.assertEqual(output, 'Sphere area : 4.1887902047863905')

    def test_main_exit_option(self):
        with mock.patch('src.challenge4.volume_calc.get_float', return_value=5):
            with mock.patch('src.challenge4.volume_calc._exit', return_value='bye'):
                output = volume_calc.main()
                self.assertEqual(output, 'bye')

    def test_main_cylinder_option(self):
        with mock.patch('src.challenge4.volume_calc.get_float', side_effect=[2, 1, 1]):
            output = volume_calc.main()
            self.assertEqual(output, 'Cylinder area : 3.141592653589793')


if __name__ == '__main__':
    unittest.main()

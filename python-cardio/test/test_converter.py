import unittest
from unittest import mock

from src.challenge3 import converter


class VolumeCalculator(unittest.TestCase):
    def setUp(self):
        self.factor_converters = {'km': 0.6213712, 'mi': 1.609344}

    def test_is_valid_input_mi(self):
        result = converter.is_valid_input('1_mi')
        self.assertTrue(result)

    def test_is_valid_input_km(self):
        result = converter.is_valid_input('1_km')
        self.assertTrue(result)

    def test_is_valid_input_false(self):
        result = converter.is_valid_input('1_m')
        self.assertFalse(result)

    def test_main_converter_mi(self):
        with mock.patch('src.challenge3.converter.get_string', return_value='1_mi'):
            expected_result = str(1 * self.factor_converters['mi'])
            result = converter.main()
            self.assertEqual(result, expected_result)

    def test_main_converter_km(self):
        with mock.patch('src.challenge3.converter.get_string', return_value='1_km'):
            expected_result = str(1 * self.factor_converters['km'])
            result = converter.main()
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

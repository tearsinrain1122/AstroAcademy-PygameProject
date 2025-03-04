from unittest import TestCase, main
from health_bar_utils import calculate_health_bar_width, ZeroOrNegativeRatio, NonNumericRatio, NonIntHealth


class TestHealthBarRatio(TestCase):

    def test_game_start_values(self):
        expected = 100
        result = calculate_health_bar_width(80, 0.8)
        self.assertEqual(expected, result)

    def test_game_end_values(self):
        expected = 0
        result = calculate_health_bar_width(0, 0.8)
        self.assertEqual(expected, result)

    def test_zero_ratio(self):
        with self.assertRaises(ZeroOrNegativeRatio):
            calculate_health_bar_width(80, 0)

    def test_str_input(self):
        with self.assertRaises(NonNumericRatio):
            calculate_health_bar_width(80, "Typo")

    def test_non_positive_input(self):
        with self.assertRaises(NonIntHealth):
            calculate_health_bar_width(50.8, 0.8)


if __name__ == '__main__':
    main()

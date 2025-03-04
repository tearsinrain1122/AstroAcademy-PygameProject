from unittest import TestCase, main
from timer_utils import convert_msecs, highest_str_time


class TestConvertMsecsFunction(TestCase):

    def test_zero(self):
        expected = "00:00:0"
        result = convert_msecs(0)
        self.assertEqual(expected, result)

    def test_large_number(self):
        expected = "99:59:9"
        result = convert_msecs(5999900)
        self.assertEqual(expected, result)

    def test_small_ms(self):
        expected = "01:02:0"
        result = convert_msecs(62023)
        self.assertEqual(expected, result)


class TestCompareStringTimesFunction(TestCase):

    def test_first_time_larger(self):
        expected = "03:08:7"
        result = highest_str_time("03:08:7", "01:10:4")
        self.assertEqual(expected, result)

    def test_second_time_larger(self):
        expected = "03:08:7"
        result = highest_str_time("01:10:4", "03:08:7")
        self.assertEqual(expected, result)

    def test_equal_times(self):
        expected = "00:01:3"
        result = highest_str_time("00:01:3", "00:01:3")
        self.assertEqual(expected, result)

    def test_zero_time(self):
        expected = "00:00:0"
        result = highest_str_time("00:00:0", "00:00:0")
        self.assertEqual(expected, result)

    def test_almost_equal_times(self):
        expected = "00:03:2"
        result = highest_str_time("00:03:2", "00:03:1")
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
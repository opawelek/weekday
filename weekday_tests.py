import unittest
from weekday import count_weekday, WrongInputException


class Tester(unittest.TestCase):
    def today_test(self):
        self.assertEqual(2, count_weekday(2017, 6, 7))

    def leap_year_test(self):
        self.assertEquals(0, count_weekday(2016, 2, 29))

    def wrong_input_test(self):
        self.assertEquals(None, count_weekday(2013, -2, 3))

    def exception_test(self):
        args = ["afesfd", 2, 3.9]
        self.assertRaises(WrongInputException, count_weekday, args)


if __name__ == '__main__':
    tester = Tester()
    tester.today_test()
    tester.leap_year_test()
    tester.wrong_input_test()
    tester.exception_test()
    # ...


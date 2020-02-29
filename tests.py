import unittest
import math
import datetime
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = 'success'
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = 'failure'
        self.assertNotEqual(expected, task.firstrun())

    def test_area_circle(self):
        self.assertEqual(math.pi, task.area_circle(1))

    def test_first_last(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual((1, 5), task.first_last(list))

    def test_date_diff(self):
        d1 = datetime.date.today()
        d2 = datetime.date.today()
        self.assertEqual(0, task.date_diff(d1, d2))


if __name__ == '__main__':
    unittest.main()

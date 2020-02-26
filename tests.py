import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = 'success'
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = 'failure'
        self.assertNotEqual(expected, task.firstrun())

    def test_area_circle(self):
        pass

    def test_first_last(self):
        pass

    def test_date_diff(self):
        pass


if __name__ == '__main__':
    unittest.main()

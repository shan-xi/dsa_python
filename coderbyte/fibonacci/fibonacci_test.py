import unittest

from fibonacci import f, is_num_fibonacci, is_num_fibonacci2, is_fibonacci_series


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_success(self):
        got = f(10)
        want = 55
        self.assertEqual(got, want)

    def test_is_num_fibonacci_success(self):
        got = is_num_fibonacci(0)
        want = True
        self.assertEqual(got, want)

    def test_is_num_fibonacci2_success(self):
        got = is_num_fibonacci2(55)
        want = True
        self.assertEqual(got, want)

    def test_is_fibonacci_series_success(self):
        got = is_fibonacci_series([2, 3, 5])
        want = True
        self.assertEqual(got, want)

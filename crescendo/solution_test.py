import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.run(1)
        exp = 1
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()

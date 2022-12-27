import unittest
from zigzag_conversion import Solution


class ZigzagConversionTest(unittest.TestCase):
    def test_case1_success(self):
        got = Solution().convert(s="PAYPALISHIRING", numRows=3)
        want = "PAHNAPLSIIGYIR"
        self.assertEqual(got, want)

    def test_case2_success(self):
        got = Solution().convert(s="PAYPALISHIRING", numRows=4)
        want = "PINALSIGYAHRPI"
        self.assertEqual(got, want)

    def test_case3_success(self):
        got = Solution().convert(s="A", numRows=1)
        want = "A"
        self.assertEqual(got, want)

    def test_case4_success(self):
        got = Solution().convert(s="ABC", numRows=1)
        want = "ABC"
        self.assertEqual(got, want)

import unittest

from bracket_matcher import BracketMatcher


class TestBracketMatcher(unittest.TestCase):
    def test_case1_success(self):
        got = BracketMatcher("(coder)(byte))")
        want = 0
        self.assertEqual(got, want)

    def test_case2_success(self):
        got = BracketMatcher("(c(oder)) b(yte)")
        want = 1
        self.assertEqual(got, want)

    def test_case3_success(self):
        got = BracketMatcher("the color re(d))()(()")
        want = 0
        self.assertEqual(got, want)

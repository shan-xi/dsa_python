import unittest

from greatest_repeated_word import find2


class GreatestRepeatedWordTest(unittest.TestCase):
    def test_testcase1_success(self):
        got = find2(["abbc", "bbabc", "abcderf"])
        want = "bbabc"
        self.assertEqual(got, want)

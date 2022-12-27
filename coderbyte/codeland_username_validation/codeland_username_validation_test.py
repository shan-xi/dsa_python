import unittest

from codeland_username_validation import CodelandUsernameValidation


class CodelandUsernameValidationTest(unittest.TestCase):
    def test_case1_success(self):
        got = CodelandUsernameValidation("aa_")
        want = False
        self.assertEqual(got, want)

    def test_case2_success(self):
        got = CodelandUsernameValidation("u__hello_world123")
        want = True
        self.assertEqual(got, want)

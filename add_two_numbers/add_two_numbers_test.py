import unittest

from add_two_numbers import Util, Solution


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers_case1_success(self):
        n1 = Util.build_single_linked_list_from_array([3, 4, 2])
        n2 = Util.build_single_linked_list_from_array([4, 6, 5])
        actual = Util.string_result(Solution().addTwoNumbers(n1, n2))
        expected = "708"
        self.assertEqual(actual, expected)

    def test_add_two_numbers_case2_success(self):
        n1 = Util.build_single_linked_list_from_array([0])
        n2 = Util.build_single_linked_list_from_array([0])
        actual = Util.string_result(Solution().addTwoNumbers(n1, n2))
        expected = "0"
        self.assertEqual(actual, expected)

    def test_add_two_numbers_case3_success(self):
        n1 = Util.build_single_linked_list_from_array([9, 9, 9, 9, 9, 9, 9])
        n2 = Util.build_single_linked_list_from_array([9, 9, 9, 9])
        actual = Util.string_result(Solution().addTwoNumbers(n1, n2))
        expected = "89990001"
        self.assertEqual(actual, expected)
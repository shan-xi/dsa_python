import unittest

from leetcode_2130 import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        node = ListNode(5)
        node.next = ListNode(4)
        node.next.next = ListNode(2)
        node.next.next.next = ListNode(1)
        ans = s.pairSum(node)
        exp = 6
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        node = ListNode(4)
        node.next = ListNode(2)
        node.next.next = ListNode(2)
        node.next.next.next = ListNode(3)
        ans = s.pairSum(node)
        exp = 7
        self.assertEqual(ans, exp)

    def test_case3(self):
        s = Solution()
        node = ListNode(1)
        node.next = ListNode(100000)
        ans = s.pairSum(node)
        exp = 100001
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()

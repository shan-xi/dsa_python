import unittest

from dsa_python.leetcode.leetcode_1302 import TreeNode
from leetcode_1302 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        node = TreeNode(1)
        node.left = TreeNode(2)
        node.right = TreeNode(3)
        node.right.right = TreeNode(6)
        node.right.right.right = TreeNode(8)
        node.left.left = TreeNode(4)
        node.left.left.left = TreeNode(7)
        node.left.right = TreeNode(5)
        ans = s.deepestLeavesSum(node)
        exp = 15
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        node = TreeNode(6)
        node.left = TreeNode(7)
        node.left.left = TreeNode(2)
        node.left.left.left = TreeNode(9)
        node.left.right = TreeNode(7)
        node.left.right.left = TreeNode(1)
        node.left.right.right = TreeNode(4)
        node.right = TreeNode(8)
        node.right.left = TreeNode(1)
        node.right.right = TreeNode(3)
        node.right.right.right = TreeNode(5)
        ans = s.deepestLeavesSum(node)
        exp = 19
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()

import unittest

from leetcode_938 import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.right = TreeNode(18)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        ans = s.rangeSumBST(root, 7, 15)
        exp = 32
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.left.right.left = TreeNode(6)
        root.left.left.left = TreeNode(1)
        ans = s.rangeSumBST(root, 6, 10)
        exp = 23
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()

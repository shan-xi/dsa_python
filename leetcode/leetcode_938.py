# 938. Range Sum of BST
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        current_sum = 0
        if low <= root.val <= high:
            current_sum += root.val
        current_sum += self.rangeSumBST(root.left, low, high)
        current_sum += self.rangeSumBST(root.right, low, high)
        return current_sum

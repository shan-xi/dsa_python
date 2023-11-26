# 1302. Deepest Leaves Sum
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            nonlocal total_sum, max_depth
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                total_sum = node.val
            elif depth == max_depth:
                total_sum += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        total_sum = 0
        max_depth = 0
        dfs(root, 0)
        return total_sum

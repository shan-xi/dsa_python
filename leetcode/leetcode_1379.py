# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # call stack version
        if not original:
            return None

        if original == target:
            return cloned

        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result

        return self.getTargetCopy(original.right, cloned.right, target)

        # explict stack version
        # if not original:
        #     return None
        #
        # stack = [(original, cloned)]
        # while stack:
        #     node_o, node_c = stack.pop()
        #     if node_o == target:
        #         return node_c
        #     if node_o.left:
        #         stack.append((node_o.left, node_c.left))
        #     if node_o.right:
        #         stack.append((node_o.right, node_c.right))
        #
        # return None

a = Solution()
t1 = TreeNode(7)
node = a.getTargetCopy(t1, t1, t1)
print(node.val)
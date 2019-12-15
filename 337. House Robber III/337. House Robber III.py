# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            left,right = dfs(node.left), dfs(node.right)
            return (max(left) + max(right), node.val + left[0] + right[0])
        return max(dfs(root))
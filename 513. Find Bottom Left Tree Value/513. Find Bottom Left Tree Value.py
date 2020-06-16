"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append(root)
        bottom_left = root.val
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == 0:
                    bottom_left = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return bottom_left
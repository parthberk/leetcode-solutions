"""
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].


Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]
        def left_boundary(root):
            if not root or not root.left and not root.right:
                return []
            if not root.left and root.right:
                return [root.val] + left_boundary(root.right)
            return [root.val] + left_boundary(root.left)
        result_leaves = []
        def leaf_nodes(root):
            nonlocal result_leaves
            if not root:
                return None
            if not root.left and not root.right:
                result_leaves.append(root.val)
                return
            leaf_nodes(root.left)
            leaf_nodes(root.right)
        def right_boundary(root):
            if not root or not root.left and not root.right:
                return []
            if not root.right and root.left:
                return right_boundary(root.left) + [root.val]
            return  right_boundary(root.right) + [root.val]
        left_result = left_boundary(root.left)
        right_result = right_boundary(root.right)
        leaf_nodes(root)
        #print(left_result,result_leaves,right_result)
        return [root.val] +  left_result + result_leaves + right_result
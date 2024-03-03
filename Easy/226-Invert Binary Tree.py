# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Approach:
# Use a recursive function to flip the binary tree. Note: This question can't be solved by level order traversal as we can't swap tree node values of
# two nodes in the same level.'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if None == root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp: TreeNode = root.left
        root.left = root.right
        root.right = temp
        return root
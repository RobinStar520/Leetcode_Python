# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Approach:
# Use DFS.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List, NoReturn

class Solution:
    def dfs(self, root: Optional[TreeNode], result: List[int]) -> NoReturn:
        if None == root:
            return
        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        self.dfs(root, result)
        return result
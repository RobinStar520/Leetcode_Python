# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105

# Approach:
# Use DFS to restore all node values to a list, and then get the minimum distance.\

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import NoReturn, List, Optional

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes: List[int] = []
        self.dfs(root, nodes)
        result: int = 999999999
        n: int = len(nodes)
        for i in range(0, n - 1):
            result = min(result, nodes[i + 1] - nodes[i])
        return result
        
    def dfs(self, root: Optional[TreeNode], nodes: List[int]) -> NoReturn:
        if None == root:
            return
        self.dfs(root.left, nodes)
        nodes.append(root.val)
        self.dfs(root.right, nodes)
        return
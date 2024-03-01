# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Approach:
# Use DFS with backtracking to get all paths from root node to leaf nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List, NoReturn

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[List[str]]:
        result: List[List[[str]]] = []
        if root is None:
            return result
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, root: Optional[TreeNode], path: str, result: List[List[str]]) -> NoReturn:
        if root.left is None and root.right is None:
            result.append(path)
            return
        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val), result)
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val), result)
        
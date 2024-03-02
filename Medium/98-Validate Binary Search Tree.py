# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Approach:
# We can use the special properties of binary search trees: the list obtained by inorder traversal is in ascending order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional, NoReturn

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr: List[int] = []
        self.dfs(root, arr)
        return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
    
    def dfs(self, root: Optional[TreeNode], arr: List[int]) -> NoReturn:
        if None == root:
            return
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)
        return
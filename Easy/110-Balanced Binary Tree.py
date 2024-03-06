# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Approach:
# Use a brute-force algorithm. For every node, check whether the node is balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional, NoReturn
from collections import deque

class Solution:
    def dfs(self, root: Optional[TreeNode], nodes: List[TreeNode]) -> NoReturn:
        if None == root:
            return
        nodes.append(root)
        self.dfs(root.left, nodes)
        self.dfs(root.right, nodes)
        return
    def get_height(self, root: Optional[TreeNode]) -> int:
        if None == root:
            return 0
        height: int = 0
        q = deque()
        q.append(root)
        while len(q) > 0:
            n: int = len(q)
            while n > 0:
                node: TreeNode = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
            height += 1
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        nodes: List[TreeNode] = []
        self.dfs(root, nodes)
        for node in nodes:
            left_height: int = self.get_height(node.left)
            right_height: int = self.get_height(node.right)
            if abs(left_height - right_height) > 1:
                return False
        return True
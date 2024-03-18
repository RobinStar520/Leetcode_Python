# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100

# Apoproach:
# Use DFS or BFS to checl whether all node values equal root.val.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        while len(q) > 0:
            n: int = len(q)
            while n > 0:
                node: TreeNode = q.popleft()
                if node.val != root.val:
                    return False
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
        return True
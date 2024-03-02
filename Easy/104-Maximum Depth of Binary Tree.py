# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Approach:
# Use BFS to get the number of binary tree levels.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth: int = 0
        q: List[TreeNode] = []
        if None == root:
            return depth
        q.append(root)
        while len(q) > 0:
            n = len(q)
            while n > 0:
                node = q.pop(0)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
            depth += 1
        return depth
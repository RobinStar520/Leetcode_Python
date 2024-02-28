# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Approach:
# This question is a premium version of question 102. In this question, we just need to recore the level index of the binary tree, and check whether
# need to reverse or not.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right  right
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        q: List[TreeNode] = []
        # Index of binary tree levels
        index = 0
        if None == root:
            return result
        q.append(root)
        while len(q) > 0:
            n = len(q)
            level = []
            while n > 0:
                node = q.pop(0)
                level.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                
                n -= 1
            if index % 2 == 1:
                level.reverse()
            index += 1
            result.append(level)
        return result
            
        
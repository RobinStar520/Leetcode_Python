# Given the root of a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:


# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100

# Approach:
# Use BFS to get the last level nodes, and then calculate the sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List
from itertools import accumulate

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        levels: List[List[TreeNode]] = []

        while len(q) > 0:
            n: int = len(q)
            level: List[TreeNode] = []

            while n > 0:
                node: TreeNode = q.popleft()
                level.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
            levels.append(level)
        return list(accumulate(levels[len(levels) - 1], initial=0)).pop(-1)

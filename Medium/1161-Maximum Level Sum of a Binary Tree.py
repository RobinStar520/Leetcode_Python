# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Approach:
# Use bianry tree level travseral algorithm(BFS).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from itertools import accumulate
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        total: float = float("-inf")
        q: List[TreeNode] = [root]
        result: int = -1
        index: int = 1
        while len(q) > 0:
            n = len(q)
            level: List[int] = []
            while n > 0:
                node = q.pop(0)
                level.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
            level_sum = list(accumulate(level, initial=0))
            if level_sum[len(level_sum) - 1] > total:
                total = level_sum[len(level_sum) - 1]
                result = index
            index += 1
        return result
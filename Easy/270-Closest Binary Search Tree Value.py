# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

# Approach:
# Save all tree nodes to a list, and then sort the list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from collections import deque

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result: int = 10001
        diff: float = float("inf")
        vals: List[int] = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            n: int = len(q)
            while n > 0:
                node = q.popleft()
                vals.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
        sorted_list = sorted(vals, key=lambda x:(abs(x-target), x))
        return sorted_list[0]
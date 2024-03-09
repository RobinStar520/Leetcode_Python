# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Approach:
# So many approachs. I used BFS with a set.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, Set

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals: Set[int] = set()
        q = deque()
        q.append(root)
        while len(q) > 0:
            n: int = len(q)
            while n > 0:
                node = q.popleft()
                if (k - node.val) in vals:
                    return True
                vals.add(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
        return False
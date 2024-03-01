# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000

# Approach:
# Use bianry tree level traversal algorithm(BFS).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result: int = 0
        q: List[TreeNode] = []
        q.append(root)
        while len(q) > 0:
            n = len(q)
            while n > 0:
                node = q.pop(0)
                
                if node.left is not None:
                    if node.left.left is None and node.left.right is None:
                        result += node.left.val
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                n -= 1
        return result
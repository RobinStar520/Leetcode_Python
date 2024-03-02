# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

# Approach:
# Same solution as question 116.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from typing import List, Optional, NoReturn

class Solution:
    def level_connect(self, level) -> NoReturn:
        n = len(level)
        for i in range(n - 1):
            level[i].next = level[i + 1]
        return

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q: List[Node] = []
        if None == root:
            return root
        q.append(root)
        while len(q) > 0:
            n = len(q)
            level: List[Node] = []
            while n > 0:
                node = q.pop(0)
                level.append(node)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                n -= 1
            self.level_connect(level)
        return root
        
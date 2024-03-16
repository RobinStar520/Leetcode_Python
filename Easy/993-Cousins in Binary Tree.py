# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.

# Approach:
# Use BFS, use a hash table to restore node's parent and level in the bianry tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Dict, Tuple, Optional
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        node_dict: Dict[int, Tuple[TreeNode, int]] = {root.val: (None, 1)}
        level: int = 1
        q = deque()
        q.append(root)
        while len(q) > 0:
            n: int = len(q)
            while n > 0:
                node: TreeNode = q.popleft()
                if node.left != None:
                    q.append(node.left)
                    node_dict[node.left.val] = (node, level + 1)
                if node.right != None:
                    q.append(node.right)
                    node_dict[node.right.val] = (node, level + 1)
                n -= 1
            level += 1
        # print(node_dict[x], node_dict[y])
        return node_dict[x][0] != node_dict[y][0] and node_dict[x][1] == node_dict[y][1]

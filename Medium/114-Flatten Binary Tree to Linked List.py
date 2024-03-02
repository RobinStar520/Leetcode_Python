# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
 

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

# Approach:
# Save all tree node to a list, and then modify the pointers of nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional, NoReturn

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list: List[TreeNode] = []
        self.dfs(root, node_list)
        for i in range(len(node_list) - 1):
            node_list[i].left = None
            node_list[i].right = node_list[i + 1]
        return
    
    def dfs(self, root: Optional[TreeNode], node_list: List[TreeNode]) -> NoReturn:
        if None == root:
            return
        node_list.append(root)
        self.dfs(root.left, node_list)
        self.dfs(root.right, node_list)
        return
        
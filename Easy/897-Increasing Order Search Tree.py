# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:


# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
 

# Constraints:

# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000

# Approach:
# Restore all nodes to a list and modity their pointers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional, NoReturn

class Solution:
    def dfs(self, root: TreeNode, nodes: List[TreeNode]) -> NoReturn:
        if None == root:
            return
        self.dfs(root.left, nodes)
        nodes.append(root)
        self.dfs(root.right, nodes)
        return

    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes: List[TreeNode] = []
        self.dfs(root, nodes)
        n: int = len(nodes)
        # for i in range(n):
        #     nodes[i].left = None
        #     nodes[i].right = None
        for i in range(n - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]
        
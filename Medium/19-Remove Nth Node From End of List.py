# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Approach:
# 1.Save all node values to a list, and then remove the target value;
# 2.Create a new linked list from the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes: List[int] = []
        while head != None:
            nodes.append(head.val)
            head = head.next
        nodes.pop(len(nodes) - n)
        dummy = ListNode(-1)
        cur = dummy
        for val in nodes:
            node = ListNode(val)
            cur.next = node
            cur = node
        return dummy.next
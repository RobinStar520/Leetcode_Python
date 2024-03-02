# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Approach:
# Save all linked list nodes to a list, then reverse the list and create a new linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list = []
        while head != None:
            temp_list.append(head.val)
            head = head.next
        temp_list.reverse()
        new_head = ListNode()
        cur = new_head
        for num in temp_list:
            node = ListNode(num)
            cur.next = node
            cur = node
        return new_head.next
        
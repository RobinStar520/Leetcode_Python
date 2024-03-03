# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Approach:
# 1. Use a set to remove duplicated numbers;
# 2. sort the set via built-in function "sorted", then we will get a sorted list;
# 3. Create a new linked list from the sorted list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Set, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique: Set[int] = set()
        while head != None:
            unique.add(head.val)
            head = head.next
        unique = sorted(unique)
        dummy = ListNode(-1)
        cur = dummy
        for num in unique:
            node = ListNode(num)
            cur.next = node
            cur = node
        return dummy.next
# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?

# Appraoch:
# Traverse the entire linked list and save the node value to a Python list, and then check whether the list can be treated as a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_value: List[int] = []
        while head is not None:
            list_value.append(head.val)
            head = head.next
        
        left: int = 0
        right: int = len(list_value) - 1
        while left <= right:
            if list_value[left] != list_value[right]:
                return False
            left += 1
            right -= 1
        return True
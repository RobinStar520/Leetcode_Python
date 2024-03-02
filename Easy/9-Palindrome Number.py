# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

# Approach:
# Use two-pointer algorithm.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        _str: str = str(x)
        length: int = len(_str)
        low: int = 0
        high: int = length - 1
        while low < high:
            if _str[low] != _str[high]:
                return False
            high -= 1
            low += 1
        return True
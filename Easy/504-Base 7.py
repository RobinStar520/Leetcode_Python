# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107

# Appraoch:
# Extract every digit of the number to a list, and then convert the list to a string.

from typing import List
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        temp: int = abs(num)
        digits: List[int] = []
        while temp > 0:
            digits.append(temp % 7)
            temp //= 7
        digits.reverse()
        result: str = ""
        if num < 0:
            result = "-"
        for digit in digits:
            result += str(digit)
        return result
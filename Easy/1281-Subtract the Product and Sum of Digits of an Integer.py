# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 

# Constraints:

# 1 <= n <= 10^5

# Approach:
# Convert the integer to string and calculate production and sum of its digits simultaneously.

from typing import List

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multiply: int = 1
        sum: int = 0
        num_str: str = str(n)
        for ch in num_str:
            multiply *= int(ch)
            sum += int(ch)
        return multiply - sum

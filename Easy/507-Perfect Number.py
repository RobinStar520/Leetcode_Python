# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

 

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false
 

# Constraints:

# 1 <= num <= 108

# Approach:
# Enumerate all perfect numbers, and use binary search to check whether a number is perfect.

import bisect
from typing import List

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        nums: List[int] = [6, 28, 496, 8128, 33550336]
        index: int = bisect.bisect_left(nums, num, 0, len(nums))
        if index != len(nums) and nums[index] == num:
            return True
        return False
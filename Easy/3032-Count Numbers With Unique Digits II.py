# Given two positive integers a and b, return the count of numbers having unique digits in the range [a, b] (inclusive).
 

# Example 1:

# Input: a = 1, b = 20
# Output: 19
# Explanation: All the numbers in the range [1, 20] have unique digits except 11. Hence, the answer is 19.
# Example 2:

# Input: a = 9, b = 19
# Output: 10
# Explanation: All the numbers in the range [9, 19] have unique digits except 11. Hence, the answer is 10. 
# Example 3:

# Input: a = 80, b = 120
# Output: 27
# Explanation: There are 41 numbers in the range [80, 120], 27 of which have unique digits.
 

# Constraints:

# 1 <= a <= b <= 1000

# Approach:
# Use brute force method. Check each number in the range [a, b].

from typing import Set

class Solution:
    def numberCount(self, a: int, b: int) -> int:
        result: int = 0
        for num in range(a, b + 1):
            if self.isValid(num):
                result += 1
        return result

    def isValid(self, num):
        _set: Set[str] = set()
        num_str = str(num)
        for ch in num_str:
            _set.add(ch)
        return len(_set) == len(num_str)
        
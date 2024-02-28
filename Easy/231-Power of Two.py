# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1

# Approach:
# Use a loop to check if an integer is a power of two.

from math import log2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            if pow(2, i) == n:
                return True
        return False
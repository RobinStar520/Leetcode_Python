# Given an integer n, return true if and only if it is an Armstrong number.

# The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

 

# Example 1:

# Input: n = 153
# Output: true
# Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
# Example 2:

# Input: n = 123
# Output: false
# Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
 

# Constraints:

# 1 <= n <= 108
# Approach:
# Follow the question description.

class Solution:
    def isArmstrong(self, n: int) -> bool:
        num: str = str(n)
        result: int = 0
        m: int = len(num)
        for ch in num:
            result += int(pow(int(ch), m))
        print(result)
        return result == n

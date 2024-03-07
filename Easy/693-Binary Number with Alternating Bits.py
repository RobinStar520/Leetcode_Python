# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
 

# Constraints:

# 1 <= n <= 231 - 1

# Approach:
# Convert the number to binary mode and check whether it has alternating bits.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_str: str = bin(n)[2:]
        for i in range(len(bin_str)):
            if i % 2 == 0:
                if bin_str[i] != '1':
                    return False
            else:
                if bin_str[i] != '0':
                    return False
        return True
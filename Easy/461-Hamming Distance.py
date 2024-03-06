# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
 

# Constraints:

# 0 <= x, y <= 231 - 1

# Approach:
# 1.Convert two integers to binary mode, and then convert them to lists.
# 2.Align two lists;
# 3.Calculate Hamming distance.

from typing import List

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b1 = list(bin(x)[2:])
        b2 = list(bin(y)[2:])
        diff: int = abs(len(b1) - len(b2))
        extra: List[int] = ['0'] * diff
        if len(b1) > len(b2):
            b2 = extra + b2
        else:
            b1 = extra + b1
        result: int = 0
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                result += 1
        return result
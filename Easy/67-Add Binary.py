# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Approach:
# 1.Convert the binary string to integer;
# 2.Add two numbers and convert the result to a binary string(Remeber to split).

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c: int = int(a, 2)
        d: int = int(b, 2)
        return bin(c + d)[2:]
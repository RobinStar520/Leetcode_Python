# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

# Example 1:

# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
# Example 2:

# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

# Constraints:

# 1 <= n <= 250

# Approach:
# Easy math problem.

class Solution:
    def countTriples(self, n: int) -> int:
        count: int = 0
        if n < 5:
            return 0
        for i in range(3, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i ** 2 + j ** 2 == k ** 2:
                        count += 1
        return count * 2

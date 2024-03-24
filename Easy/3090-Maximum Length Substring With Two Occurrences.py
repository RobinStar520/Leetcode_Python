# Given a string s, return the maximum length of a 
# substring
#  such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

# Approach:
# Using a brutral force approach. Try all substrings to find the largest one that satisfies all conditions.

from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n: int = len(s)
        result: int = -1
        for i in range(n):
            for j in range(1, n - i + 1):
                sub: str = s[i: j + i]
                c = Counter(sub)
                flag: bool = True
                for val in c.values():
                    if val > 2:
                        flag = False
                        break
                if flag == True:
                    result = max(result, len(sub))
        return result

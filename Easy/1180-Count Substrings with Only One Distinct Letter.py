# Given a string s, return the number of substrings that have only one distinct letter.

 

# Example 1:

# Input: s = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.
# Example 2:

# Input: s = "aaaaaaaaaa"
# Output: 55
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] consists of only lowercase English letters.

# Approach:
# For example: "aaaa" has 10 substrings, so we just need to calculate how many string that only contain one letter we can get.

from collections import deque

class Solution:
    def countLetters(self, s: str) -> int:
        q = deque()
        result: int = 0
        for ch in s:
            if len(q) == 0:
                q.append(ch)
                continue
            if ch == q[-1]:
                q.append(ch)
            else:
                result += (1 + len(q)) * len(q) // 2
                q.clear()
                q.append(ch)
        if len(q) != 0:
            result += (1 + len(q)) * len(q) // 2
        return result

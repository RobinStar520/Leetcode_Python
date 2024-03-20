# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.

# Approach:
# Use a queue and greedy approach: If the queue is empty, push character to the it, otherwise get the number of elements in the queue and clear it.

from collections import deque

class Solution:
    def maxPower(self, s: str) -> int:
        q = deque()
        result: int = 0
        for ch in s:
            if len(q) == 0:
                q.append(ch)
                continue
            else:
                if ch == q[-1]:
                    q.append(ch)
                else:
                    result = max(result, len(q))
                    q.clear()
                    q.append(ch)
        if len(q) != 0:
            result = max(len(q), result)
        return result
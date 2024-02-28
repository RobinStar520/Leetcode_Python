# Given a string s, return true if a permutation of the string could form a 
# palindrome
#  and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

# Approach:
# Count the frequency of each letter in the string. If a string is a palindrome, it can only have no more than one letter that appear in odd times.

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        count: int = 0
        for k, v in counter.items():
            if v % 2 == 1:
                count += 1
            if count > 1:
                return False

        return True
# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: s = "aeiou"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.

# Approach:
# Use a for-loop.

class Solution:
    def is_vowel(self, ch: str) -> bool:
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

    def removeVowels(self, s: str) -> str:
        result: str = ""
        for ch in s:
            if not self.is_vowel(ch):
                result += ch
        return result
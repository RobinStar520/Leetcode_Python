# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

# Approach:
# Use a stack to store all vowels.

from typing import List
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack: List[str] = []
        for ch in s:
            if self.isVowel(ch):
                stack.append(ch)
        print(stack)
        result: str = ""
        for ch in s:
            if self.isVowel(ch):
                result += stack.pop()
            else:
                result += ch
        return result

    def isVowel(self, ch: str) -> bool:
        ch = ch.lower()
        return ch == 'a' or ch == 'i' or ch == 'o' or ch == 'e' or ch =='u'
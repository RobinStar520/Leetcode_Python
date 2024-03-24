# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
 

# Constraints:

# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.

# Approach:
# Using two-pointer technique.

class Solution:
    def is_vowel(self, ch: str) -> bool:
        ch = ch.lower()
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
    def halvesAreAlike(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1
        l_count: int = 0
        r_count: int = 0
        while left <= right:
            if self.is_vowel(s[left]):
                l_count += 1
            if self.is_vowel(s[right]):
                r_count += 1
            left += 1
            right -= 1
        # print(l_count, r_count)
        return l_count == r_count

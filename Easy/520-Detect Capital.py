# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.

# Approach:
# Count the number of uppercase and lowercase letters.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper: int = 0
        lower: int = 0
        for ch in word:
            if ch.islower():
                lower += 1
            else:
                upper += 1
        n: int = len(word)
        if upper == n or lower == n:
            return True
        if word[0].isupper() and upper == 1:
            return True
        return False
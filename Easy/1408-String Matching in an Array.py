# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.

# Approach:
# Use brute-force approach. Checking whether a word is a substring of another word in the list.

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        n: int = len(words)
        result: List[str] = []
        print(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    result.append(words[i])
        return list(set(result))

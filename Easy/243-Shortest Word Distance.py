# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
 

# Constraints:

# 2 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2

# Approach:
# Collecting the index of word1 and word2 in the "wordDict", and then use two loops to find the shortest distance between two words.

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_list: List[int] = []
        word2_list: List[int] = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1_list.append(i)
            elif wordsDict[i] == word2:
                word2_list.append(i)
        result: int = 999999

        for i in range(len(word1_list)):
            for j in range(len(word2_list)):
                result = min(result, abs(word1_list[i] - word2_list[j]))
        return result
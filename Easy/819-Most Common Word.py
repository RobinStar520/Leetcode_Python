# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"
 

# Constraints:

# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.

# Approach:
# This question is easy enough, but need to pay attention to some details.

from typing import List, Dict
class Solution:
    # def collect_word(self, word_list: List[str]) -> NoReturn:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # In order to separate words, we need to append a whitespace to the string.
        paragraph += " "
        freq_dict: Dict[str, int] = {}
        word: str = ""
        # Extract words.
        for ch in paragraph:
            if ch.isalpha():
                word += ch
            else:
                word = word.lower()
                if word in freq_dict:
                    freq_dict[word] += 1
                else:
                    freq_dict[word] = 1
                word = ""
        # Remove whitespace from the dictionary.
        if "" in freq_dict:
            freq_dict.pop("")
        # print(freq_dict)
        freq: int = -1
        result: str = ""
        for k, v in freq_dict.items():
            if k not in banned:
                if v > freq:
                    freq = v
                    result = k
        return result
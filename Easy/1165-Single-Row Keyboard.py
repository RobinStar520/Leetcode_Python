# There is a special keyboard with all keys in a single row.

# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

 

# Example 1:

# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4. 
# Example 2:

# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# Output: 73
 

# Constraints:

# keyboard.length == 26
# keyboard contains each English lowercase letter exactly once in some order.
# 1 <= word.length <= 104
# word[i] is an English lowercase letter.

# Approach:
# Use a dictionary to save the reflection between letter and the index.

from typing import Dict

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        index_dict: Dict[str, int] = {}
        for i in range(len(keyboard)):
            index_dict[keyboard[i]] = i
        print(index_dict)
        result: int = index_dict[word[0]]
        for i in range(1, len(word)):
            result += abs(index_dict[word[i]] - index_dict[word[i - 1]])
        return result
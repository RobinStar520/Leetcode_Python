# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Appraoch:
# Sort the list and use a greedy algorithm to find the longet common prefix.

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result: str = ""
        index: int = 0
        str1 = strs[0]
        str2 = strs[len(strs) - 1]
        while index < len(str1) and str1[index] == str2[index]:
            result += str1[index]
            index += 1
        return result
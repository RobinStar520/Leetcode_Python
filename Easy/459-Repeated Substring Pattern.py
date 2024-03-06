# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# # s consists of lowercase English letters.

# Approach:
# 1.Create an integer variable n equal to the length of s;
# 2.Iterate over all the prefix substrings of length i = 1 to n / 2:
# If i divides n, we declare an empty string pattern. Use an inner loop that iterates n / i times to concatenate the substring formed from the first i characters of s.
# If pattern equals s, we return true.
# 3.There is no substring that can be repeated to form s. As a result, we return false.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            part: str = s[:i]
            times = len(s) // len(part)
            if times * part == s:
                return True
        return False
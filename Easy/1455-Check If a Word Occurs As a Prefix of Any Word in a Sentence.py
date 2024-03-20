# Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

# A prefix of a string s is any leading contiguous substring of s.

 

# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
# Example 2:

# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
# Example 3:

# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.
 

# Constraints:

# 1 <= sentence.length <= 100
# 1 <= searchWord.length <= 10
# sentence consists of lowercase English letters and spaces.
# searchWord consists of lowercase English letters.

# Approach:
# Use trie to check whether current word is prefix of a existing word.

class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.is_end: bool = False

class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()
    
    def insert(self, word: str):
        cur: TrieNode = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    
    def starts_with(self, word: str) -> bool:
        cur: TrieNode = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words: list = sentence.split()
        trie: Trie = Trie()
        # for word in words:
        #     trie.insert(word)
        n: int = len(words)
        for i in range(n):
            trie.insert(words[i])
            if trie.starts_with(searchWord) == True:
                return i + 1
        return -1
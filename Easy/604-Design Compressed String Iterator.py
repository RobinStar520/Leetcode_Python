# Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

# Implement the StringIterator class:

# next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
# hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
 

# Example 1:

# Input
# ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
# [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
# Output
# [null, "L", "e", "e", "t", "C", "o", true, "d", true]

# Explanation
# StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
# stringIterator.next(); // return "L"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "t"
# stringIterator.next(); // return "C"
# stringIterator.next(); // return "o"
# stringIterator.hasNext(); // return True
# stringIterator.next(); // return "d"
# stringIterator.hasNext(); // return True
 

# Constraints:

# 1 <= compressedString.length <= 1000
# compressedString consists of lower-case an upper-case English letters and digits.
# The number of a single character repetitions in compressedString is in the range [1, 10^9]
# At most 100 calls will be made to next and hasNext.

# Approach:
# 1. Extract numbers and letters pairwisely.
# 2. Use a deque as queue.

from typing import List
from collections import deque

class StringIterator:

    def __init__(self, compressedString: str):
        self.q = deque()
        n: int = len(compressedString)
        index: int = 0
        letter: str = ""
        while index < n:
            number: str = ""
            if compressedString[index].isalpha():
                letter = compressedString[index]
                index += 1
            else:
                while index < n and compressedString[index].isnumeric():
                    number += compressedString[index]
                    index += 1
                self.q.append([letter, int(number)])
        
        

    def next(self) -> str:
        if self.hasNext():
            item: List[str | int] = self.q[0]
            ch: str = item[0]
            self.q[0][1] -= 1
            if self.q[0][1] == 0:
                self.q.popleft()
            return ch
        return " "

    def hasNext(self) -> bool:
        return len(self.q) != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
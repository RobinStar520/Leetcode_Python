# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]
 

# Constraints:

# 1 <= left <= right <= 104

# Approach:
# 1. Generate a list from [left, right];
# 2. Filter data.


from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        temp: List[int] = [i for i in range(left, right + 1)]
        return list(filter(self.is_selfDividing, temp))
        
    def is_selfDividing(self, number: int) -> bool:
        num: str = str(number)
        if '0' in num:
            return False
        for ch in num:
            if number % int(ch) != 0:
                return False
        return True
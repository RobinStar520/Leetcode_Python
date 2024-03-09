# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

# Approach:
# Use a counter object to count the frequency of numbers; Use binary search to find the missing value.

from typing import List
import bisect
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        nums.sort()
        result: List[int] = []
        for k, v in c.items():
            if v == 2:
                result.append(k)
                break
        n: int = len(nums)
        for i in range(1, n + 1):
            index: int = bisect.bisect_left(nums, i, 0, n)
            if index == n or nums[index] != i:
                result.append(i)
        return result
# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# Example 2:

# Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
# Output: []
 

# Constraints:

# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000

# Approach:
# Use binary search to find whether a numer is in a list.

from typing import List
from bisect import bisect_left

class Solution:
    def bianry_search(self, arr: List[int], target: int) -> int:
        index: int = bisect_left(arr, target)
        if index != len(arr) and arr[index] == target:
            return index
        return -1

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result: List[int] = []
        for num in arr1:
            if self.bianry_search(arr2, num) >= 0 and self.bianry_search(arr3, num) >= 0:
                result.append(num)
        return result
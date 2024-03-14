# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

# Example 1:

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
 

# Constraints:

# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.

# Approach:
# 1.Use a hash map to restore element indexes;
# 2.Sort the list and check whether the last element is twice larger than the previous one.

from typing import List, Dict

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index_dict: Dict[int, int] = {}
        n: int = len(nums)
        for i in range(n):
            index_dict[nums[i]]= i
        nums.sort()
        if nums[n - 2] * 2 <= nums[-1]:
            return index_dict[nums[-1]]
        return -1
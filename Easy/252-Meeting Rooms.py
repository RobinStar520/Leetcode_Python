# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: true
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106

# Approach:
# Use a greedy algorithm to check whether there is a range which is a subset of another one.

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
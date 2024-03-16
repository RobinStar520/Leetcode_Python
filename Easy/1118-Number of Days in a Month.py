# Given a year year and a month month, return the number of days of that month.

 

# Example 1:

# Input: year = 1992, month = 7
# Output: 31
# Example 2:

# Input: year = 2000, month = 2
# Output: 29
# Example 3:

# Input: year = 1900, month = 2
# Output: 28
 

# Constraints:

# 1583 <= year <= 2100
# 1 <= month <= 12

# Approach:
# Check whether the year is leap.

import calendar
from typing import Dict

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days: Dict[int, int] = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if calendar.isleap(year):
            days[2] = 29
        return days[month]
        

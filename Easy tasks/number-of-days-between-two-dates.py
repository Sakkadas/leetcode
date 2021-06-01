"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

"""


import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y, m, d = list(map(int, date1.split('-')))
        y1, m1, d1 = list(map(int, date2.split('-')))
        res1 = datetime.date(y, m, d)
        res2 = datetime.date(y1, m1, d1)
        return abs((res1 - res2).days)


if __name__ == "__main__":
    s = Solution()
    print(s.daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))

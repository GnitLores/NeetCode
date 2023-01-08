from calendar import monthrange


class Solution:
    # In order for a year to qualify as a leap year, it must be divisible by 4. If it is a centurial year, it must also be divisible by 400.
    def dayOfYear(self, date: str) -> int:
        days_pr_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        # Add an extra day to febuary if leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_pr_month[1] += 1

        return sum(days_pr_month[: month - 1]) + day


sol = Solution()
print(sol.dayOfYear(date="2019-01-09"))
print(sol.dayOfYear(date="2019-02-10"))

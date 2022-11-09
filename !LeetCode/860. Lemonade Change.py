import collections
from typing import List


class Solution:
    # Greedy solution using dictionary to count bills available.
    # For every transactions, return as many bills as possible
    # in descending order (a 20 is harder return than two 10s,
    # and there is no situation where a 20 can be returned but
    # two 10s cannot, so it is always better to return
    # the larger bill).
    # If there is still change remaining when all possible bills
    # have been given as change, return False. Otherwise True.
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = collections.defaultdict(int)
        price = 5

        def returnBills(change, val):
            while change >= val and count[val] > 0:
                change -= val
                count[val] -= 1
            return change

        for bill in bills:
            count[bill] += 1
            change = bill - price
            if change == 0: continue
            
            change = returnBills(change, 20)
            change = returnBills(change, 10)
            change = returnBills(change, 5)
            if change > 0: return False

        return True

sol = Solution()
print(sol.lemonadeChange(bills = [5,5,5,10,20]))
print(sol.lemonadeChange(bills = [5,5,10,10,20]))
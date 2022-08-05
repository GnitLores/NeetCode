class Solution(object):
    # Iterate through list of prices and store best profit
    # If a cheaper buy price is found, use that buy price in future calculations.
    # O(n) time and faster than 96.7% of solutions.
    def maxProfit(self, prices):
        bestProfit = 0

        for day in range(0, len(prices)):
            price = prices[day]
            if day == 0:
                buyPrice = price
                continue
            
            if price < buyPrice:
                buyPrice = price
            else:
                profit = price - buyPrice
                if profit > bestProfit and profit > 0:
                    bestProfit = profit
        return bestProfit

def testSolution(*args):
    sol = Solution
    result = sol.maxProfit(sol, *args)
    print(": " + str(result))

testSolution([7,1,5,3,6,4])
testSolution([7,6,4,3,1])
import collections

# Greedy solution.
# If the sum of gas is greater than the sum of costs, there must be a solution.
# If there is a solution, that solution is unique as per the constraints.
# Iterate through tracking the running sum of difference between gas and cost.
# If it is negative, we can disregard anything before that as a start point.
# Try next start point and reset running sum.
# There is no need to continue looping over because we have already guaranteed that there is a solution.
# O(n)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) - sum(cost) < 0:
            return -1
        
        currentStart = 0
        currentSum = 0
        for i in range(len(gas)):
            currentSum += gas[i] - cost[i]
            if currentSum < 0:
                currentStart = i + 1
                currentSum = 0

        return currentStart
        
        


sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(sol.canCompleteCircuit([2,3,4], [3,4,3]))
print(sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
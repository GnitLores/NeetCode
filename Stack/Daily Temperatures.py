class Solution(object):
    # The key is to realize, thatfor a day we have not yet found a hotter day for,
    # when we do find a hotter day, it will also be hotter than all days in between.
    # This means that we can iterate through, storing the temperature and index of day on a stack.
    # Then we compare subsequent days to the top of the stack, and calculate the difference in days.
    # Keep popping days from the stack until the top is not colder than the current day.
    # O(n) time.
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        idx = []
        stack.append(temperatures[0])
        idx.append(0)
        for i in range(1, len(temperatures)):

            while len(stack) > 0 and temperatures[i] > stack[-1]:
                stack.pop()
                old = idx.pop()
                res[old] = i - old
                
            stack.append(temperatures[i])
            idx.append(i)
        return res

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
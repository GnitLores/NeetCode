class Solution:
    # Each step can only be reached from the two previous steps, both in a single distinct way.
    # Consequently, the number of possible ways is the sum of number of ways to reach those steps.
    # O(n) time.
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1] # Step one is in index zero

    # Same but constant extra space. Similar results on leetcode.
    def climbStairsConstantSpace(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        twoBefore = 1
        oneBefore = 2
        for _ in range(2, n):
            steps = twoBefore + oneBefore
            twoBefore = oneBefore
            oneBefore = steps
        return steps

sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(10))
print("")
print(sol.climbStairsConstantSpace(2))
print(sol.climbStairsConstantSpace(3))
print(sol.climbStairsConstantSpace(10))
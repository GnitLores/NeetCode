class Solution:
    # Dynamic programming solution
    #
    # Observation:
    # If a zero occurs, only two outcomes are possible.
    # If there is no number before it, or the number before is not 1 or 2, it violates the encoding and we can return 0.
    # If 1 or 2 comes before, this MUST be a two digit number 10 or 20.
    # Consequently, we can split the problem into two simpler problems:
    # the number of possible configurations to the left and right of this fixed number.
    # If we do this for all zeros, we end up with smaller strings that cannot contain zero.
    #
    # This simplifies the dynamic programming problem.
    # Obervation:
    # If we add a number, there are two cases:
    # A - it is a valid second digit (two digits <= 26).
    # B - it is not a valid second digit.
    # If we treat it as the second digit of a number, the combinations possible are the same as ways_n-2.
    # If not, the combinations possible are the same as ways_n-1.
    # Thus, if it is a valid second digit, the combinations are (ways_n-1 + ways_n-2).
    # If not the combinations are just ways_n-1.
    #
    # O(n) time.
    def numDecodings(self, s: str) -> int:
        s = [int(c) for c in s] # Work on lists instead of input string

        # Identify all zeros and split numbers into smaller lists around fixed numbers if this is a valid list.
        split = []
        sub = []
        for i in range(len(s)):
            if s[i] == 0:
                if i == 0:
                    return 0
                else:
                    if 1 <= s[i - 1] <= 2:
                        sub.pop() # remove first digit of fixed number from sublist
                        split.append(sub.copy())
                        sub = []
                    else:
                        return 0
            else:
                sub.append(s[i])
        if s[i] != 0:
            split.append(sub.copy())

        # Dynamic programming function for use on simpler sublist without zeros.
        def countWays(nums):
            if len(nums) < 2:
                return 1

            twoBefore = 1 # one combination pr default
            oneBefore = 1
            for i in range(1, len(nums)):
                if i > 0 and (((10 * nums[i - 1]) + nums[i]) <= 26):
                    ways = oneBefore + twoBefore
                else:
                    ways = oneBefore
                twoBefore = oneBefore
                oneBefore = ways

            return ways

        # Find combinations of all simpler sublists and multiply them
        ways = 1
        for nums in split:
            ways *= countWays(nums)

        return ways

    # Dynamic programming solution without zero removal simplification.
    #
    # Observation:
    # When we encounter a zero, if it is valid then there is only one option for both
    # itself and the preceding number. Concequently, both ways_n and ways_n-1 must be the same as ways_n-2.
    # In effect we have to retroactively update n-1 with the new information the 0 provides.
    # Makes the splitting unnecessary but also makes the DP algorithm quite a bit more complicated.
    # We also have to deal with a few more edge cases.
    # O(n) time.
    def numDecodingsNoSimplification(self, s: str) -> int:
        nums = [int(c) for c in s] # Work on lists instead of input string
        if len(nums) == 1 and nums[0] == 0:
            return 0
        if len(nums) < 2:
            return 1

        twoBefore = 1
        oneBefore = 1
        ways = 1
        for i in range(0, len(nums)):
            if i == 0:
                if nums[i] == 0:
                    return 0
                else:
                    continue
            
            if nums[i] == 0:

                if not (nums[i - 1] == 1 or nums[i - 1] == 2): # is zero valid?
                    return 0
                else:
                    ways = oneBefore = twoBefore # retroactively update

            elif nums[i - 1] != 0 and ((10 * nums[i - 1]) + nums[i]) <= 26: # we now have to check for zeros in preceding number
                ways = oneBefore + twoBefore

            else:
                ways = oneBefore

            twoBefore = oneBefore
            oneBefore = ways

        return ways

sol = Solution()
print(sol.numDecodings("10"))
print(sol.numDecodings("12"))
print(sol.numDecodings("226"))
print(sol.numDecodings("06"))
print(sol.numDecodings("2101"))
print(sol.numDecodings("162101325"))
print("")
print(sol.numDecodingsNoSimplification("10"))
print(sol.numDecodingsNoSimplification("12"))
print(sol.numDecodingsNoSimplification("226"))
print(sol.numDecodingsNoSimplification("06"))
print(sol.numDecodingsNoSimplification("2101"))
print(sol.numDecodingsNoSimplification("162101325"))
from typing import List


class Solution:
    # Dynamic programming solution.
    # A brute force solution involves many repeated calculations.
    # Instead we can store intermediate results in a set, and check
    # if a result ever equals the target value which is sum/2.
    # Since we reject all values greater than the target, the set
    # can have at most sum/2 number of values.
    #
    # O(n*sum) time, which is much more efficient that the
    # brute force solution which would be O(2^n). However,
    # if the total sum is very large it will not be efficient.
    # Runs very efficiently on leetcode.
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        sums = set()
        sums.add(0)
        for i in range(len(nums)):
            newSums = set()
            for s in sums:
                tmp = nums[i] + s
                if tmp == target: # Immediately stop if we find target
                    return True
                elif tmp < target: # Only allow values smaller than target
                    newSums.add(tmp)
            sums.update(newSums)
        return False



sol = Solution()
print(sol.canPartition([1,5,11,5]))
print(sol.canPartition([1,2,3,5]))
class Solution(object):
    # Iterate over the array with pointer indicating first value.
    # Apply the Two Sum II two-pointer solution array to the right of main pointer.
    # The main problem is that we don't want duplicates like [-1, 1, 0] [1, 0, -1].
    # To avoid this, iterate the main pointer as well the left pointer if the hit the same value twice.
    # The right pointer will automatically have to move in response.
    # O(n^2) time.
    def threeSum(self, nums):
        nums.sort()
        res = []
        for ptr1 in range(len(nums)):
            if ptr1 > 0 and nums[ptr1] == nums[ptr1-1]: # Iterate main pointer to avoid duplicates
                continue
            l = ptr1 + 1
            r = len(nums) - 1
            
            while l < r:
                threeSum = nums[ptr1] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[ptr1], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # Iterate left pointer to avoid duplicates
                        l += 1

        return res
    
def testSolution(*args):
    sol = Solution()
    res = sol.threeSum(*args)
    print(res)

testSolution([-1,0,1,2,-1,-4])
testSolution([0,1,1])
testSolution([0,0,0])
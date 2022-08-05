class Solution(object):
    # In a loop, check the middle value.
    # If it is not the target, check if the target should be before or after.
    # Update the indices and repeat for either earlier or later part of list.
    # Repeat until target is found or only one value that is not the target remains.
    # O(logn) time and faster than 64.1% of solutions.
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        
        while True:
            midpoint = (start+end) // 2
            if nums[midpoint] == target:
                return midpoint
            if start == end:
                return -1

            if target > nums[midpoint]:
                start = min(midpoint+1,len(nums))
            else:
                end = max(midpoint-1,0)


def testSolution(*args):
    sol = Solution
    result = sol.search(sol, *args)
    print(": " + str(result))

testSolution([-1,0,3,5,9,12], 5)
testSolution([-1,0,3,5,9,12], 9)
testSolution([-1,0,3,5,9,12], 2)
testSolution([-1,0,3,5,9,12], -1)
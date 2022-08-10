class Solution(object):
    # Two pointers pointing at lowest and hight value.
    # If sum is greater than target, move right pointer left -> smaller sum.
    # If sum is smaller than taget, move left pointer right -> greater sum.
    # Works because input is sorted.
    # O(n) time and constant extra space.
    def twoSum(self, numbers, target):
        ptr1 = 0
        ptr2 = len(numbers)-1

        while not (numbers[ptr1] + numbers[ptr2]) == target:
            if (numbers[ptr1] + numbers[ptr2]) > target:
                ptr2 -= 1
            else:
                ptr1 += 1

        return [ptr1+1, ptr2+1]

def testSolution(*args):
    sol = Solution()
    res = sol.twoSum(*args)
    print(res)

testSolution([2,7,11,15], 9)
testSolution([2,3,4], 6)
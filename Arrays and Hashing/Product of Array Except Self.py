class Solution(object):
    # Make two lists of intermediate results containing products up to that element running from left and right.
    # The ouput of an element is previous left result * the following right result.
    # O(n) time and no use of division.
    def productExceptSelf(self, nums):

        # Calculate intermediate products from left and right.
        # The right product is calculated on a reversed list.
        numsReversed = list(reversed(nums))
        leftProducts = [0]*len(nums)
        rightProducts = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                leftProducts[i] = nums[i]
                rightProducts[i] = numsReversed[i]
            else:
                leftProducts[i] = leftProducts[i-1] * nums[i]
                rightProducts[i] = rightProducts[i-1] * numsReversed[i]
        rightProducts = list(reversed(rightProducts))

        # Multiply left and right products for each element:
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = rightProducts[i+1]
            elif i == len(nums)-1:
                res[i] = leftProducts[i-1]
            else:
                res[i] = leftProducts[i-1]*rightProducts[i+1]
        return res
    
    # The principle of the first solution was correct, but it can actually be done without using extra memory and in less code.
    # However, this migt be less readable.
    # The intermediate results (prefix and postfix) are multiplied together and stored directly in the output.
    # O(n) time and constant extra memory.
    def productExceptSelfSimple(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

def testSolution(*args):
    sol = Solution()
    res = sol.productExceptSelf(*args)
    print(res)
    res = sol.productExceptSelfSimple(*args)
    print(res)

testSolution([1,2,3,4])
testSolution([-1,1,0,-3,3])
testSolution([-1,1,0,-3,3,0])
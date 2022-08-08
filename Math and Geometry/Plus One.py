class Solution(object):
    # Iterative inter based solution.
    # Iterate backwards incrementing.
    # As long as there is carry over, keep adding.
    # If no carry over, the operation is complete.
    # Do a final check to see if the most signicant digit carried over.
    # If so, insert the carry over in new most significant place.
    def plusOne(self, digits):

        for i in range(len(digits))[::-1]: # Use extended slicing to iterate backwards.
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        
        if digits [0] == 0:
            digits.insert(0, 1)

        return digits

        

def testSolution(*args):
    sol = Solution()
    res = sol.plusOne(*args)
    print(str(res))

testSolution([1,2,3])
testSolution([4,3,2,9])
testSolution([9,9,9,9])
testSolution([9])
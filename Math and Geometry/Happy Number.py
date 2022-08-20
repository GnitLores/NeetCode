class Solution(object):
    # If finding the sum of squares results in a state that happened previously, an infinite cycle will occur.
    # Save each state in a hashtable, and check if there is a repetition.
    # As long as it does not repeat, continue until 1 is reached.
    def isHappy(self, n):
        def decompose(n):
            sum = 0
            while n > 0:
                digitValue = n % 10 # Find the ones digit value with modulus
                sum += digitValue**2 # Add square of value to sum
                n = n // 10 # Use floor division by 10 to move next digit to ones digit
            return sum
        
        previousStates = set()
        while n not in previousStates:
            previousStates.add(n)
            n = decompose(n)
            if n == 1: return True
        
        return False
    

def testSolution(*args):
    sol = Solution()
    res = sol.isHappy(*args)
    print(str(res))

testSolution(19)
testSolution(2)
import math

class Solution(object):
    # Strip non-alphanumeric characters and convert to lower case.
    # Run two pointers through from beginning and end and compare chars until the pointers meet.
    # O(n) time. Doesn't run on leetcode because of the preprocessing.
    def isPalindrome(self, s):
        s = "".join(filter(str.isalnum, s)).lower()
        i = 0
        k = len(s)-1
        while i < k:
            if s[i] != s[k]:
                return False
            i += 1
            k -= 1
        return True
    
    # Runs on leetcode, but is a bit more complicated.
    # No preprocessing, use loop for each pointer within the main loop to move pointers until valid character is found or pointers meet.
    # O(n) time and faster than 35.5% of solutions.
    def isPalindromeNoPreprocessing(self, s):
        i = 0
        k = len(s)-1
        while i < k:
            while i < k and not self.isAlphaNumeric(s[i]):
                i += 1
            while k > i and not self.isAlphaNumeric(s[k]):
                k -= 1
            if s[i].lower() != s[k].lower():
                return False
            i += 1
            k -= 1
        return True

    def isAlphaNumeric(c):
        return (("a" <= c.lower() <= "z") or ("0" <= c <= "9"))


def testSolution(s):
    sol = Solution
    result = sol.isPalindrome(sol, s)
    print("Preprocessing: " + str(result))
    result = sol.isPalindromeNoPreprocessing(sol, s)
    print("No preprocessing: " + str(result))

testSolution("A man, a plan, a canal: Panama")
testSolution("Lool")
testSolution("race a car")
testSolution(" ")
class Solution:
    # Use helper function that identifies all divisors of string.
    # The string itself is a divisor.
    # For all substrings starting from the first char and up to half
    # the length of the string:
    # If the length of the string is divisible by the length of the substring,
    # the substring is a divisor if the string is equal to the substring repeated
    # to be as long as the string.
    #
    # Find all divisors of both strings and check which is the longest common divisor.
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def findDivisors(s):
            divisors = {s}
            for i in range(0, len(s) // 2):
                divLen = i + 1
                if len(s) % divLen != 0: continue
                div = s[0:divLen]
                if s == div * (len(s) // divLen):
                    divisors.add(div)
            return divisors

        common = findDivisors(str1).intersection(findDivisors(str2))
        common.add("")
        return max(common, key = len)

sol = Solution()
print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
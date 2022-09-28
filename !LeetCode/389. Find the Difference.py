import collections


class Solution:
    # Solution using bit manipulation.
    # XORing two identical numbers gives zero.
    # XORing zero and a number gives the number.
    # The order in which the numbers are XORed does not matter.
    # Consequently, XORing all the numbers cancels out all numbers that appear an even number of times.
    # The result will be the only number that does not have a duplicate.
    def findTheDifferenceBitManipulation(self, s: str, t: str) -> str:
        res = 0
        for c in s:
            res = res ^ ord(c)
        for c in t:
            res = res ^ ord(c)
        return chr(res)

    # Solution using dictionary to count characters.
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = collections.defaultdict(int)
        for c in t:
            cnt[c] += 1

        for c in s:
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]

        return list(cnt.keys())[0]

sol = Solution()
print(sol.findTheDifferenceBitManipulation(s = "abcd", t = "abcde"))
print(sol.findTheDifferenceBitManipulation(s = "", t = "y"))
print("")
print(sol.findTheDifference(s = "abcd", t = "abcde"))
print(sol.findTheDifference(s = "", t = "y"))
import collections


class Solution:
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
print(sol.findTheDifference(s = "abcd", t = "abcde"))
print(sol.findTheDifference(s = "", t = "y"))
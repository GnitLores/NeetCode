import collections


class Solution:
    # Count letters with dictionary and decrement letters in note.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = collections.defaultdict(int)

        for c in magazine:
            cnt[c] += 1

        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False

        return True

sol = Solution()
print(sol.canConstruct(ransomNote = "a", magazine = "b"))
print(sol.canConstruct(ransomNote = "aa", magazine = "ab"))
print(sol.canConstruct(ransomNote = "aa", magazine = "aab"))
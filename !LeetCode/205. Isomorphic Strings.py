class Solution:
    # Three things can happend that cause strings to not be ismomorphic:
    # 1 - Unequal length
    # 2 - The same char in a string maps to multiple different chars.
    # 3 - Multiple chars in a string maps to the same char.
    #
    # This solution uses a dictionary to test condition 2 for each char,
    # and a set to test condition 3.
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charmap = dict()
        mapped = set()
        for c1, c2 in zip(s, t):
            if c1 in charmap:
                if c2 != charmap[c1]: # If condition 2 doesn't hold
                    return False
            else:
                if c2 in mapped: # If condition 3 doesn't hold
                    return False
                else:
                    charmap[c1] = c2
                    mapped.add(c2)
        return True

sol = Solution()
print(sol.isIsomorphic(s = "egg", t = "add"))
print(sol.isIsomorphic(s = "foo", t = "bar"))
print(sol.isIsomorphic(s = "paper", t = "title"))
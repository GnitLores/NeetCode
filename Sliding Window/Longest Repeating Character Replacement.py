class Solution:
    # Sliding window solution.
    # Runs for each character in input.
    # For each chracter run a sliding window over the string.
    # Make up to two substitutions and let window grow.
    # When no more substitutions left, make left pointer catch up to first substitution.
    # Record maximum window size.
    # O(n) time but not very elegant or efficient.
    def characterReplacement(self, s: str, k: int) -> int:
        chars = ''.join(set(s)) # Unique characters in s
        res = 0

        for c in chars:
            subs = 0
            l = 0
            w = 0
            while l + w < len(s):
                if s[l + w] != c:
                    if subs == k: # If no more substitutions
                        while l < len(s) and s[l] == c: # Move l up to last sub
                            l += 1
                            w -= 1
                        l += 1 # And past the last sub
                        w -= 1
                    else:
                        subs += 1
                w += 1
                res = max(res, w)
        return res

def testSolution(*args):
    sol = Solution()
    res = sol.characterReplacement(*args)
    print(res)

testSolution("ABAB", 2)
testSolution("AABABBA", 1)
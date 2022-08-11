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

    # Solution that uses a hashmap.
    # Iterate the right point over array, counting chars in hashmap.
    # Check if count is valid given the number of possible replacements.
    # Instead of doing everything for each character, just use the character with greates count in window.
    # If window is invalid, move left pointer right until it is valid again.
    # Also O(n) but more efficient and simple.
    def characterReplacementHashmap(self, s: str, k: int) -> int:
        res = 0
        counts = dict()
        
        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

    # Optimized solution.
    # It is not necessary to scan the hashmap to find the max frequency.
    # If the frequency is lower than previously, the result will not be improved anyway.
    # Just keep track of a global max frequency.
    def characterReplacementMaxFrequency(self, s: str, k: int) -> int:
        res = 0
        counts = dict()
        
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxFreq = max(maxFreq, counts[s[r]])

            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
    
def testSolution(*args):
    sol = Solution()
    res = sol.characterReplacement(*args)
    print(res)
    res = sol.characterReplacementHashmap(*args)
    print(res)
    res = sol.characterReplacementMaxFrequency(*args)
    print(res)

# testSolution("ABAB", 2)
testSolution("AABABBA", 1)
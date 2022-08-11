class Solution(object):
    # Use a hashset as a sliding window, and add characters to the hashset.
    # If a character already exist, remove character up to and including the previous occurrence  that character.
    # Add new character, and record maximum set size.   
    # O(n) time.
    def lengthOfLongestSubstring(self, s):
        
        res = 0
        hashset = set()
        l = 0
        for c in s:
            if c in hashset:
                isFound = False
                while not isFound:
                    if s[l] == c:
                        isFound = True
                    hashset.remove(s[l])
                    l += 1
                    
            hashset.add(c)
            res = max(res, len(hashset))

        return res

    # Exact same algorithm but simpler implementation of character removal loop.
    def lengthOfLongestSubstringSimple(self, s):
    
        res = 0
        hashset = set()
        l = 0
        for c in s:
            while c in hashset:
                hashset.remove(s[l])
                l += 1
                    
            hashset.add(c)
            res = max(res, len(hashset))

        return res

def testSolution(*args):
    sol = Solution()
    res = sol.lengthOfLongestSubstring(*args)
    print(res)
    res = sol.lengthOfLongestSubstringSimple(*args)
    print(res)

testSolution("abjpooespfmbuyrcabcbb")
testSolution("abcabcbb")
import collections

class Solution:
    # Sliding window solution.
    # First:
    # - Grow window to the right until we find a matching substring.
    # - Shrink that window from the left so long as it matches.
    # - This is the initial window.
    # Repeatedly:
    # - Slide window to the right until we find a matching substring again.
    # - Try to shrink window from the left while maintaining match.
    # - Record minimum matching window length.
    #
    # The tricky part is to find the substring match in constant time. Matching strings would be linear time.
    # Count the characters of the target string with dictionary. This is our match target - how many of each char we need.
    # Every time we add a char to window, decrement the count of that char if it is in the dictionary.
    # Every time we remove a char from window, increment the count.
    # If we remove a char and decrement from 1 to 0 - this char is now a match. Increment the number of matching chars.
    # If we add a char and increment from 0 to 1 - this char is no longer a match. Decrement the number of matching chars.
    # If the number of matching chars = the number chars in the dictionary, the substring is matching.
    # If we add more instances of a char than we need the target count will become negative.
    # This doesn't matter, it is still a match. It is only the change in count from 0 to 1 and 1 to 0 that matters.
    #
    # O(n) time because substring matching happens in constant time. Efficient on leetcode.
    def minWindow(self, s: str, t: str) -> str:

        # Count chars to search for
        matchTarget = collections.defaultdict(int)
        for i in range(len(t)):
            matchTarget[t[i]] += 1
        nMatching = [0]
        
        # Add char to window and update count
        def addChar(r):
            if s[r] in matchTarget:
                matchTarget[s[r]] -= 1
                if matchTarget[s[r]] == 0:
                    nMatching[0] += 1

        # Remove char to window and updating count
        def removeChar(l):
            if s[l] in matchTarget:
                    matchTarget[s[l]] += 1
                    if matchTarget[s[l]] == 1:
                        nMatching[0] -= 1
        
        def windowMatches():
            return nMatching[0] == len(matchTarget)

        # Grow initial matching window to the right:
        l = 0
        r = 0
        while r < len(s) and not windowMatches():
            addChar(r)
            r += 1
        r -= 1
        
        # If there is no matching substring
        if not windowMatches():
            return ""

        # Shrink initial matching window from left
        if windowMatches():
            while s[l] not in matchTarget or matchTarget[s[l]] < 0:
                removeChar(l)
                l += 1
            substring = s[l:r + 1]

        # Try to find a smaller window
        while r < len(s) - 1:
            
            # Slide window right
            removeChar(l)
            l += 1
            r += 1
            addChar(r)

            # Once a match is found, shrink window from left as long as it matches
            if windowMatches():
                while s[l] not in matchTarget or matchTarget[s[l]] < 0:
                    removeChar(l)
                    l += 1
                substring = s[l:r+1]
        
        return substring

    # Neetcode solution.
    # They used a very similar idea.
    # Instead of sliding the window, they repeatedly grow it right until there is a matcj
    # and shrink from left until it is no longer a match.
    # Instead incrementing and decrementing the count of chars to look for,
    # they use two dictionaries, one for the target count and one for the window count.
    # They can then just compare the relevant char in each dictionary.
    # Only chars that are being looked for are counted in both dictionaries.
    # Similarly to my own solution, they maintain a count of matching characters.
    # Also O(n) time.
    def minWindowSimpleComparison(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

sol = Solution()
print(sol.minWindow(s = "IKADOBECODEBANCHK", t = "ABC"))
print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(sol.minWindow(s = "a", t = "a"))
print(sol.minWindow(s = "a", t = "aa"))
print(sol.minWindow(s = "bba", t = "ab"))
print(sol.minWindow(s = "aaflslflsldkalskaaa", t = "aaa"))
print("")
print(sol.minWindowSimpleComparison(s = "IKADOBECODEBANCHK", t = "ABC"))
print(sol.minWindowSimpleComparison(s = "ADOBECODEBANC", t = "ABC"))
print(sol.minWindowSimpleComparison(s = "a", t = "a"))
print(sol.minWindowSimpleComparison(s = "a", t = "aa"))
print(sol.minWindowSimpleComparison(s = "bba", t = "ab"))
print(sol.minWindowSimpleComparison(s = "aaflslflsldkalskaaa", t = "aaa"))
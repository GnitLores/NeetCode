class Solution:
    # Geekforgeeks solution using rolling hash (Rabin Karp Algorithm).
    # Calculate a hash function for the needle that can be updated character
    # by character.
    # Calculate the same hash function for a running window,
    # ans whenever the hash function matches, check character by character for
    # a match.
    # Char values are set to ascii values.
    # When sliding the window, the leftmost (most significant char) is removed
    # by subtracting its hash value at the most significant position.
    # The remaining chars are shifted to more significant positions by multiplying
    # hash by h, and a new least significant char is then added.
    # The size of the prime number determines how many collisions will occur.
    # Technically O(m*n) like brute force solution, but in practice very few
    # collissions should occur, making it close to O(n). Very efficient on leetcode.
    def strStrRollingHash(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
            
        base = 26 # the number of characters in the input alphabet
        prime = 101 # A prime number
        win = len(needle)
        n = len(haystack)
        nHash = 0    # hash value for pattern
        wHash = 0    # hash value for txt
        
        # The value of h would be "pow(base, win-1)% q"
        h = 1
        for i in range(win-1):
            h = (h * base) % prime
    
        # Calculate the hash value of pattern and first window
        # of text
        for i in range(win):
            nHash = (base * nHash + ord(needle[i])) % prime
            wHash = (base * wHash + ord(haystack[i])) % prime
    
        # Slide the pattern over text one by one
        for i in range(n - win + 1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters one by one
            if nHash == wHash:
                for j in range(win):
                    if haystack[i + j] != needle[j]:
                        break
                j += 1
                if j == win:
                    return i
    
            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < n-win:
                wHash = (base*(wHash-ord(haystack[i])*h) + ord(haystack[i + win])) % prime
    
                # We might get negative values of hash, converting it to
                # positive
                if wHash < 0:
                    wHash = wHash + prime
            
        return -1

    # Semi-brute force solution.
    # Look for matches of first char in needle.
    # If match is found, search for subsequent chars of needle.
    # If all match, return index of first char.
    # In principle this is O(m*n) worst case, but in practice it
    # should usually be closer to O(n) because we do not match the entire
    # needle string. We only match subsequent characters if previous ones match.
    # It is very efficient when testing on leetcode.
    def strStrBruteForce(self, haystack: str, needle: str) -> int:
        for i, c in enumerate(haystack):
            if c == needle[0]:
                j = 0
                while i + j < len(haystack) and haystack[i + j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                    j += 1
        return -1

sol = Solution()
print("")
print(sol.strStrRollingHash(haystack = "mississippi", needle = "sippi"))
print(sol.strStrRollingHash(haystack = "mississippi", needle = "issi"))
print(sol.strStrRollingHash(haystack = "sadbutsad", needle = "sad"))
print(sol.strStrRollingHash(haystack = "leetcode", needle = "leeto"))
print("")
print(sol.strStrBruteForce(haystack = "mississippi", needle = "sippi"))
print(sol.strStrBruteForce(haystack = "mississippi", needle = "issi"))
print(sol.strStrBruteForce(haystack = "sadbutsad", needle = "sad"))
print(sol.strStrBruteForce(haystack = "leetcode", needle = "leeto"))
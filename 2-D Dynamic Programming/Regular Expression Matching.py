class Solution:
    # Neetcode's solution using recursion and memoization.
    # The main issue is dealing with the "*" operator.
    # We use two pointers, i in the string and j in the pattern.
    # We check if the current char matches the current pattern char
    # and if it does, we check if it is followed by a star.
    # If there is a star following a matching char, we can include any amount
    # of that character.
    # This means that we recursively call the search for both of those choices,
    # and if any of them lead to a match, this is a match.
    # If we choose to not include the character again, we move j 2 to the right,
    # as we want to skip beyond the the "*" operator.
    # If we choose to include the character again, we move i 1 to the right and check
    # for the next character.
    # Since the "*" operator allows us to use a char zero times, it is actually possible for
    # i to go out of bounds for a string that is a valid match.
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p): # If both i and j go out of bounds, we have succesfully matched the entire string.
                return True
            if j >= len(p): # If pattern ends while there are still chars in the string, this is not a matching string.
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # Any character matches the "." operator
            if (j + 1) < len(p) and p[j + 1] == "*": # If the matching character is followed by a "*" operator
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j))) # This is a match if we can find a match either not using or using some number of chars with the "*" operator
                return cache[(i, j)]

            if match: # If there is a match without a "*" operator we simply increment both i and j to go to next char
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False # If not a match
            return False


        return dfs(0, 0)

sol = Solution()
print(sol.isMatch(s = "aa", p = "a"))
print(sol.isMatch(s = "aa", p = "a*"))
print(sol.isMatch(s = "ab", p = ".*"))
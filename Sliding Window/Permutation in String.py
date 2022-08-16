import collections

class Solution(object):
    # Solution using hashmap as sliding window.
    # Use a dictionary of the same length as the string we are looking for permutations of.
    # Count characters similarly to the Valid Anagram problem.
    # Decrement count of characters that are no longer in the window.
    # If the character couts of the searchs string and window are identical, there is a matching permutaion.
    # O(n) time.
    def checkInclusion(self, s1, s2):
        i = 0
        r = i + len(s1) - 1
        counts = dict()
        s1Counts = dict()
        while r < len(s2):
            if i == 0:
                for k in range(i,r + 1):
                    counts[s2[k]] = counts.get(s2[k], 0) + 1
                    s1Counts[s1[k]] = s1Counts.get(s1[k], 0) + 1
            else:
                counts[s2[i - 1]] -= 1
                counts[s2[r]] = counts.get(s2[r], 0) + 1
                if counts[s2[i - 1]] == 0: # Pop characters with zero occurrences so that we can test for equality later.
                    counts.pop(s2[i - 1])


            if counts == s1Counts:
                return True

            i += 1
            r = i + len(s1) - 1

        return False

sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("adc", "dcda"))
print(sol.checkInclusion("adc", "dcdda"))
from collections import defaultdict

class Solution(object):
    # Solution counting the occurrences of letters in words.
    # Input constrained to lower case letters.
    # Count of letters is used as a key in dictionary.
    # The dictionary values are the groups of strings.
    # O(m*n) time (number of strings and mean length of strings)
    def groupAnagrams(self, strs):
        asciiOffset = ord("a")
        hashmap = dict()

        for s in strs:
            charCount = [0] * 26 # There are 26 lower case letters possible
            for c in s:
                charCount[ord(c) - asciiOffset] += 1 # Use numerical ascii value of char to index character count
            charCount = tuple(charCount) # A list is not hashable, so convert to tuple

            if charCount in hashmap:
                hashmap[charCount].append(s)
            else:
                hashmap[charCount] = [s]

        return list(hashmap.values())

    # Even simpler solution that relies on the defaultdict class.
    # The dictionary defaults to lists as values.
    def groupAnagramsDefault(self, strs):
        hashmap = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord("a")] += 1

            hashmap[tuple(charCount)].append(s)

        return list(hashmap.values())

    # Naive solution using the same principle as Valid Anagram.
    # For each string, create a hashmap counting letters.
    # Compare to each existing anagram hashmap.
    # Add string to corresponding group of strings.
    # If no anagram match, create new anagram hashmap and new group of strings.
    def groupAnagramsNaive(self, strs):

        # Create hashmap counting letters of string:
        def createHashmap(s):
            hashmap = dict()
            for c in s:
                if c in hashmap:
                    hashmap[c] = hashmap[c] + 1
                else:
                    hashmap[c] = 1
            return hashmap

        # Handle empty and single string input:
        if not strs:
            return []
        if len(strs) == 1:
            return [strs]
        str = strs.pop()
        anagrams = [createHashmap(str)]
        groupedStrs = [[str]]

        # Handle all strings after first:
        for i in range(0, len(strs)):
            str = strs[i]
            hashmap = createHashmap(str)

            groupNr = 0
            anagramFound = False
            while groupNr < len(anagrams):
                if hashmap == anagrams[groupNr]:
                    groupedStrs[groupNr].append(str)
                    anagramFound = True
                groupNr += 1

            if not anagramFound:
                anagrams.append(hashmap)
                groupedStrs.append([str])
        
        return groupedStrs
    
        

def testSolution(*args):
    sol = Solution()
    res = sol.groupAnagrams(*args)
    print(res)
    res = sol.groupAnagramsDefault(*args)
    print(res)
    res = sol.groupAnagramsNaive(*args)
    print(res)

# testSolution(["jabzczaf"])

testSolution(["eat","tea","tan","ate","nat","bat"])
# testSolution([""])
# testSolution(["a"])
class Solution(object):
    # Sort both strings and check if equal.
    # O(nlogn) time.
    def isAnagramUsingSorting(self, s, t):
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s == t

    # Count occurences of characters and store in dictionaries with char as key and occurences as value. Check if equal.
    # O(n) time.
    def isAnagramUsingHashing(self, s, t):
        sHashtable = self.createHashmap(s)
        tHashtable = self.createHashmap(t)
        return sHashtable == tHashtable
    
    def createHashmap(s):
        hashmap = dict()
        for c in s:
            if c in hashmap:
                hashmap[c] = hashmap[c] + 1
            else:
                hashmap[c] = 1
        return hashmap

def testSolution(s, t):
    sol = Solution
    result = sol.isAnagramUsingSorting(sol, s, t)
    print("Sorting method: " + str(result))
    result = sol.isAnagramUsingHashing(sol, s, t)
    print("Hashing method: " + str(result))

testSolution("anagram", "nagaram")
testSolution("rat", "car")
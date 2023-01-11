import collections


class Solution:
    # Three conditions must be true:
    # There must be as many letters in the patters as there are words.
    # The same letter must always be mapped to the same word.
    # The same word must always be mapped to the same letter (that is, different letters can't map to the same word).
    #
    # We use a dictionary to map letters to words and a set of uniqe words to ensure that
    # the same word doesn't get mapped to twice by different letters.
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = collections.defaultdict(str)
        uniqueWords = set()
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for i, c in enumerate(pattern):
            if c in wordMap:
                if wordMap[c] != words[i]:
                    return False
            else:
                if words[i] in uniqueWords:
                    return False
                wordMap[c] = words[i]
                uniqueWords.add(words[i])

        return True


sol = Solution()
print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))
print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))
print(sol.wordPattern(pattern="aaaa", s="dog cat cat dog"))

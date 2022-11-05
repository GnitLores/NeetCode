from collections import Counter

class Solution:
    # Replace punctuation marks with space, just removing can result in words being joined
    # (e.g "b,b" becoming ["bb"] instead of ["b", "b"]").
    # Enforce lower case, split into list of words separated by spaces, and count distinct words.
    # Delete all the banned words from the count and return the word with the highest count.
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = Counter(paragraph.lower().split())

        for w in banned:
            del count[w]
        return count.most_common()[0][0]


sol = Solution()
print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(sol.mostCommonWord(paragraph = "a.", banned = []))
print(sol.mostCommonWord(paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"]))
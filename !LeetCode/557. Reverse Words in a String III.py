class Solution:
    # Split string on spaces and join list of reversed substrings
    # with space as separator. 
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split()])

sol = Solution()
print(sol.reverseWords(s = "Let's take LeetCode contest"))
print(sol.reverseWords(s = "God Ding"))
print(sol.reverseWords(s = "Ding"))

class Solution:
    # Check if ascii value is in range of capital letters, and if
    # so add the constant interval between the ascii values of upper
    # and lower case letters (32) and convert that to char.
    def toLowerCase(self, s: str) -> str:
        def toLower(c):
            ascii = ord(c)
            if 65 <= ascii <= 90:
                c = chr(ascii + 32)
            return c
        return "".join([toLower(c) for c in s])

    def toLowerCaseCheating(self, s: str) -> str:
        return s.lower()

sol = Solution()
print(sol.toLowerCase(s = "Hello"))
print(sol.toLowerCase(s = "here"))
print(sol.toLowerCase(s = "LOVELY"))
print(sol.toLowerCase(s = "al&phaBET"))
print("")
print(sol.toLowerCaseCheating(s = "Hello"))
print(sol.toLowerCaseCheating(s = "here"))
print(sol.toLowerCaseCheating(s = "LOVELY"))
print(sol.toLowerCaseCheating(s = "al&phaBET"))
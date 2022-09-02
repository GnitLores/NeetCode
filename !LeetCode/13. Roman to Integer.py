class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        subtract = {
            "C": ("M", "D"),
            "X": ("L", "C"),
            "I": ("V", "X")
            }

        def addChar(c, i):
            if c in subtract:
                if i < len(s) - 1:
                    if s[i + 1] == subtract[c][0] or s[i + 1] == subtract[c][1]:
                        return -hm[c]
            return hm[c]
                
        res = 0
        for i, c in enumerate(s):
            res += addChar(c, i)
 
        return res

sol = Solution()
print(sol.romanToInt("MMMMCD"))
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
from typing import List


class Solution:
    # Backtracking solution using a dictionary to map numbers to letters.
    # For each possible letter, recursively call the function for the next letter.
    # Add to output when no more letters.
    # O(n * 4^n) time.
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",}
        
        res = []
        
        def findPermutations(i, perm):
            if i >= len(digits):
                res.append("".join(perm.copy()))
                return
            
            letters = letterMap[digits[i]]
            for l in letters:
                perm.append(l)
                findPermutations(i + 1, perm)
                perm.pop()

        findPermutations(0, [])
        return res


sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
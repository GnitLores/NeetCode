from typing import List

class Solution:
    # Backtracking solution.
    # In a recursive function:
    # Iterate over the string.
    # If the i first letters are a palindrom, add to a list and find palindromes in remainder of string.
    # When a palindrome is found and there are no more letters, add partition to output.
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def findPalindromes(s, palindromes):
            for i, _ in enumerate(s):

                sub = s[0:i+1]
                if sub == sub[::-1]: # If substring is a palindrome

                    palindromes.append(sub)
                    if i >= len(s) - 1: # If valid palindrome partitioning - add to output
                        res.append(palindromes.copy())
                    else: # Else look for more palindromes
                        findPalindromes(s[i+1:], palindromes)
                    palindromes.pop()
        
        findPalindromes(s, [])
        return res
            

sol = Solution()
print(sol.partition("aab"))
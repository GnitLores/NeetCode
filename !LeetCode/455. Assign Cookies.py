from tokenize import cookie_re
from typing import List


class Solution:
    # Sort both arrays in descending order because we need to
    # assign biggest cookies to most greedy children first so we
    # don't waste a big cookie on a child that is not very greedy.
    #
    # For each cookie starting from the largest, search for the most
    # greedy child that it can be assigned to and proceed to next cookie.
    #
    # O(log n) because we need to sort.
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        kid = 0
        cookie = 0
        while cookie < len(s) and kid < len(g):
            while kid < len(g) and s[cookie] < g[kid]:
                kid += 1
            
            if kid < len(g) and s[cookie] >= g[kid]:
                kid += 1
                cookie += 1
                content += 1

        return content

sol = Solution()
print(sol.findContentChildren(g = [1,2,3], s = [1,1]))
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))
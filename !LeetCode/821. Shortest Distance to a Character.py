class Solution:
    # The distance at any element is the minimum of the distance to the left and the distance to the right.
    # We can use a function to find the distance moving left to right, and then reuse the function for the
    # reversed list and reverse the output to find the distance moving from right to left.
    # Then we just need the min of those distances.
    # O(n) time.
    def shortestToChar(self, s: str, c: str) -> list[int]:
        def directionalDist(st):
            res = [None] * len(s)
            dist = float("inf")
            for i, x in enumerate(st):
                if x == c:
                    dist = 0
                else:
                    dist += 1
                res[i] = dist
            return res

        return [min(r, l) for r, l in zip(directionalDist(s), directionalDist(s[::-1])[::-1])]

sol = Solution()
print(sol.shortestToChar(s = "loveleetcode", c = "e"))
print(sol.shortestToChar(s = "aaab", c = "b"))
class Solution:
    # Create a hashset of jewel types and count how many stones are represented
    # in the set.
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(list(jewels))
        return sum([s in jewelSet for s in stones])

sol = Solution()
print(sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(sol.numJewelsInStones(jewels = "z", stones = "ZZ"))
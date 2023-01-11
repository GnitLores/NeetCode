class Solution:
    # If there are 1-3 stones on your turn, you can win.
    # If there are 4 stones, you lose, because no matter what you remove
    # the opponent can then reach 0.
    # If there are 5-7 stones on your turn, you win because you can set the
    # opponent up to have 4 stones, making them lose.
    # If there are 8 stones on your turn, you lose because no matter what you
    # remove, the opponent can set you up to have 4 left.
    #
    # This continues, meaning that you lose if there is a multiple of 4 stones
    # left on your turn.
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


sol = Solution()
print(sol.canWinNim(n=4))
print(sol.canWinNim(n=1))
print(sol.canWinNim(n=2))

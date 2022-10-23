class Solution:
    # Sum up x and y coordinate changes for all moves and see if
    # the both sum to zero.
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for c in moves:
            match c:
                case "U":
                    y -= 1
                case "D":
                    y += 1
                case "L":
                    x -= 1
                case "R":
                    x += 1
        return x == 0 and y == 0

sol = Solution()
print(sol.judgeCircle(moves = "UD"))
print(sol.judgeCircle(moves = "LL"))
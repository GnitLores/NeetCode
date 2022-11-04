class Solution:
    # Use ascii values to index characters into widths.
    # Sum widths, starting from a new line every time the max width
    # is exceeded.
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current = 0
        widths = [widths[ord(c) - ord("a")] for c in s]
        for w in widths:
            current += w
            if current > 100:
                lines += 1
                current = w
                
        return [lines, current]

sol = Solution()
print(sol.numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))
print(sol.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))
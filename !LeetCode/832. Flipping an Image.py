class Solution:
    # Invert by casting boolean not to int and reverse order row by row.
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i, row in enumerate(image):
            image[i] = [int(not x) for x in row[::-1]]
        return image

sol = Solution()
print(sol.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))
print(sol.flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
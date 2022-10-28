import collections
from typing import List


class Solution:
    # Breadth first search solution with queue.
    # Record the original color at the start position.
    # If the color to fill in, just return the image, filling in the same color
    # will change nothing and will result in an infinite loop unless visited pixels
    # are tracked.
    # Otherwise, starting from the first pixel, change the color and check if the adjacent pixels
    # are in bounds and of the original color. If so add them to the queue and continue.
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]
        if color == startColor: return image

        rows = len(image)
        cols = len(image[0])
        q = collections.deque()
        q.append((sr, sc))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if row >= 0 and row < rows and col >= 0 and col < cols:
                    if image[row][col] == startColor:
                        q.append((row, col))
        return image

sol = Solution()
print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
print(sol.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))
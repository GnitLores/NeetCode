from typing import List


class Solution:
    # Store a list of eight relative coordinate changes, which when summing
    # to a set of coordinates gives the eight surrounding cells.
    # For each cell, iterate through relative coordinates, calculate surrounding
    # coordinates for that cells, check that they are in bound, and sum up.
    # Store the average value for each cell in output array. 
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        res = []
        for r in range(rows):
            res.append([])
            for c in range(cols):
                sum = img[r][c]
                cells = 1
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if row >= 0 and row < rows and col >= 0 and col < cols:
                        sum += img[row][col]
                        cells += 1
                res[r].append(sum // cells)
                    
        return res

sol = Solution()
print(sol.imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))
print(sol.imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]]))
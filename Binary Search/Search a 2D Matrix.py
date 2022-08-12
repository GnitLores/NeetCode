from typing import List


class Solution:
    # First do a binary search on the rows of the matrix.
    # Then do a a binary serch on the values of that row.
    # Both O(logn) operations for a total of O(logn) time.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        minRow = 0
        maxRow = len(matrix)-1
        while minRow != maxRow:
            midpoint = (minRow + maxRow) // 2
            if matrix[midpoint][-1] < target:
                minRow = midpoint + 1
            else:
                maxRow = midpoint
        nums = matrix[minRow]

        start = 0
        end = len(nums)-1
        while start <= end:
            midpoint = (start+end)//2
            if nums[midpoint] == target:
                return True
            if target < nums[midpoint]:
                end = midpoint - 1
            else:
                start = midpoint + 1
                
        return False



def testSolution(*args):
    sol = Solution()
    res = sol.searchMatrix(*args)
    print(res)

testSolution([[1,3,5,7,8,9,10,11,12,13,14,15,16,17]],6)
testSolution([[1,3,5,7]],1)
testSolution([[1,3,5,7]],8)
testSolution([[1,3,5,7],[8,10,12,500]],8)
testSolution([[1,3,5,7],[8,10,12,500]],11)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 7)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60)
testSolution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 8)
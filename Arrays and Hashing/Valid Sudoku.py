import collections


class Solution(object):
    def isValidSudoku(self, board):
        
        rowSets = collections.defaultdict(set)
        columnSets = collections.defaultdict(set)
        boxSets = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue
                
                boxRow = r // 3
                boxCol = c // 3
                if val in boxSets[boxRow, boxCol]:
                    return False
                else:
                    boxSets[boxRow, boxCol].add(val)

                if val in rowSets[r]:
                    return False
                else:
                    rowSets[r].add(val)

                if val in columnSets[c]:
                    return False
                else:
                    columnSets[c].add(val)
                    
        return True

sol = Solution()

board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))

board = [
     ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))
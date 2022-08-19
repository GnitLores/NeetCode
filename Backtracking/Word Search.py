from typing import List


class Solution:
    # Recursive DFS backtracking solution.
    # This runs very slowly if for example the board is all 'A's
    # and the word is a long list of 'A' followed by a 'B'.
    # There is no solution but there are a huge amount of possible permutations to look through
    # before coming to that conclusion.
    # I made a preliminary check that counts characters to see if the board is even valid in the first place.
    # This is not required at all to get the correct answer but made the code go from
    # timing out on leetcode to being faster than 95% of answers.
    # The Neetcode solution is similar and times out on that test case as well.
    # O(n * m * 4^wl) time.
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # Preliminary check:
        boardCount = dict()
        wordCount = dict()
        for r in range(rows):
            for c in range(cols):
                boardCount[board[r][c]] = boardCount.get(board[r][c], 0) + 1
        for i in range(len(word)):
                wordCount[word[i]] = wordCount.get(word[i], 0) + 1

        for i in range(len(word)):
            if word[i] not in boardCount or wordCount[word[i]] > boardCount[word[i]]:
                return False

        # Actual recursive search.
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def findWord(r, c, idx):
            if idx >= len(word): return
            if board[r][c] != word[idx]: return

            visited.add((r, c))
            if len(visited) == len(word):
                return True

            for dr, dc in directions:
                rNew = r + dr
                cNew = c + dc
                if rNew in range(rows) and cNew in range(cols):
                    if (rNew, cNew) not in visited:
                        res = findWord(rNew, cNew, idx + 1)
                        if res == True:
                            return True

            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    res = findWord(r, c, 0)
                    if res == True:
                        return True

        return False

sol = Solution()

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]
print(sol.exist(board, "ABCCED"))

board = [
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"]]
print(sol.exist(board, "AAAAAAAAAAAABAA"))
    
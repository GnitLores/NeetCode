from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    # Used to prune a word once it has been found for better performance.
    def pruneWord(self, word) -> None:
        cur: TrieNode = self
        nodeAndChildKey: list[tuple[TrieNode, str]] = []
        for char in word:
            nodeAndChildKey.append((cur, char))
            cur = cur.children[char]

        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return

        
class Solution:
    # Neetcode solution.
    # Similar dfs approach to naive solution below, but also making use of a trie.
    # All target words are added to trie so they can be searched for simultaneously.
    # This way, common prefixes can be searched for once, and only once the words diverge
    # does the dfs diverge as well.
    # A dfs is started from each tile. Continue as long as the dfs mactches a word in the trie.
    # However, this is no longer enough to pass on leetcode.
    # More difficult test cases have been added.
    # Now it is also necessary to prune words that have been found, which is a more complicated operation.
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visit = [], set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                board[r][c] not in node.children or (r, c) in visit):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.append(word)
                node.isWord = False
                root.pruneWord(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return res

    # First attempt, naive solution.
    # Works well, but isn't fast enough to pass on leetcode.
    # The are test cases with a large amount of very similar target words.
    # We need to use a trie to process these efficiently.
    # Make dictionary mapping each alphabet letter to tiles.
    # Make array of dictionaries mapping tiles to connected letters.
    # Do a dfs for each valid start position for each target word.
    def findWordsNaive(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        letters = collections.defaultdict(list)
        tiles = [[collections.defaultdict(list) for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                letters[board[r][c]].append((r, c))
                tiles[r][c] = collections.defaultdict(list)
                if r - 1 >= 0:      tiles[r][c][board[r - 1][c]].append((r - 1, c))
                if r + 1 < rows:    tiles[r][c][board[r + 1][c]].append((r + 1, c))
                if c - 1 >= 0:      tiles[r][c][board[r][c - 1]].append((r, c - 1))
                if c + 1 < cols:    tiles[r][c][board[r][c + 1]].append((r, c + 1))

        res = set()

        visiting = set()
        def dfs(coords, w, i):
            if coords in visiting: return
            if w in res: return
            if i == len(w) - 1:
                res.add(w)
                return

            i = i + 1
            visiting.add(coords)
            if w[i] in tiles[coords[0]][coords[1]]:
                for newCoords in tiles[coords[0]][coords[1]][w[i]]:
                    dfs(newCoords, w, i)
            visiting.remove(coords)

        for w in words:
            if w[0] in letters:
                for coords in letters[w[0]]:
                    dfs(coords, w, 0)
        

        return list(res)

sol = Solution()
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(sol.findWords(board, words))
print(sol.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]))
print(sol.findWords(board = [["a","a"]], words = ["a"]))
print("")
print(sol.findWordsNaive(board, words))
print(sol.findWordsNaive(board = [["a","b"],["c","d"]], words = ["abcb"]))
print(sol.findWordsNaive(board = [["a","a"]], words = ["a"]))
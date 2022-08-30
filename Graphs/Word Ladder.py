from typing import List
import collections

class Solution:
    # BFS solution using dictionaries and sets to build adjacency list.
    # The search is a BFS, but instead of running continuously, it iteratively expands the frontier.
    # The shortest path length is the number of frontier expansions it takes to reach the target word.
    #
    # The complicated part is building the adjacency lists.
    # First, add the n-length source word to the list.
    # Make n dictionaries, one for each char index.
    # Each dictionary maps letters to the set of indices of words that have that letter at that char index.
    # For each word we then find the n sets of words that match the n letters of the word.
    # For each letter, we then add the intersection of all these sets to the adjacency set, EXCEPT for set
    # of the letter itself.
    # Finally we remove the index of the word itself from the set.
    # This way, we get a list of sets for each word, and each set contains the indices of the words that match all letters except one.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if len(beginWord) == 1:
            return 2

        endIdx = wordList.index(endWord)
        beginIdx = len(wordList)
        wordList.append(beginWord)

        # Dictionaries mapping letters at positions to sets of word indices with those letters at those positions:
        dicts = [collections.defaultdict(set) for _ in range(len(beginWord))]
        for i, w in enumerate(wordList):
            for j, c in enumerate(w):
                dicts[j][c].add(i)

        connections = [set() for _ in range(len(wordList))] # List of adjacency sets
        for i, w in enumerate(wordList):
            sharedLetters = [dicts[j][c] for j, c in enumerate(w)] # Sets of words that match each letter of this word
            for j, c in enumerate(w): # For each letter of the word:
                connections[i].update(set.intersection(*[x for k, x in enumerate(sharedLetters) if k != j])) # Add intersection of all sets except the letter itself
            connections[i].remove(i) # Remove the word itself from the adjacency set

        # BFS iteratievly expanding frontier and counting expansions.
        def bfs(source, target):
            visited = set()
            queue = collections.deque()

            visited.add(source)
            queue.append(source)
            i = 1

            while queue:
                i += 1
                for _ in range(len(queue)): # Process current frontier
                    w = queue.popleft()
                    
                    for n in connections[w]:
                        if n == target:
                            return i
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)
            return 0
        return bfs(beginIdx, endIdx)

    # Neetcode solution.
    # Create a dictionary and for each word, map patterns with a letter blanked out to the word itself.
    # The results in blanked out patterns resulting from multiple words being mapped to all those words.
    # For example:
    # "*og" : "dog", "log", "cog"
    # "d*g" : "dog"
    # "do*" : "dog", "dot"
    # In the BFS, for each word we can then just recreate these patterns from the word and find the
    # adjacent words in the dictionary.
    # 
    # Both solutions pass on leetcode, but this is simpler and more efficient.
    def ladderLengthPattern(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

sol = Solution()
print(sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
print(sol.ladderLength(beginWord = "a", endWord = "c", wordList = ["a","b","c"]))
print("")
print(sol.ladderLengthPattern(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(sol.ladderLengthPattern(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
print(sol.ladderLengthPattern(beginWord = "a", endWord = "c", wordList = ["a","b","c"]))
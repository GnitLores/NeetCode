import collections
from typing import List


class Solution:
    # Since the words are lexographically ordered, we know that their ordering is based
    # on the first differing character.
    # There is no need to compare all words to all words, we can just compare them in
    # pairs in one iteration and find the first differing character.
    # Use this to build the adjacency list of a graph.
    #
    # We can then find the order of the letters (vertices) by doing a topological sort
    # of this graph (see Course Schedule II problem). If we detect a cycle, there is no
    # unambigous ordering.
    # A topological sort finds end vertices first, so I made the adjacency list indicate
    # greater lexigraphical ordering and not smaller. Otherwise the output would just
    # have to be reversed.
    def alien_order(self, words: List[str]) -> str:
        if not words: return ""
        if len(set(words)) == 1: 
            return "".join(set(c for c in words[0]))

        # Build adjacency list
        adjacencies = collections.defaultdict(set)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjacencies[w2[j]].add(w1[j])

        # Toplogical sort
        res = []
        visiting = set()
        completed = set()
        cycleFound = [False]
        def dfs(letter):
            if letter in completed or cycleFound[0] == True:
                return

            if letter in visiting:
                cycleFound[0] = True
                return

            visiting.add(letter)
            while adjacencies[letter]:
                dfs(adjacencies[letter].pop())
            visiting.remove(letter)

            res.append(letter)
            completed.add(letter)
            return
        
        letters = list(adjacencies.keys())
        for l in letters:
            dfs(l)

        if cycleFound:
            res.append("")
        
        return "".join(res)
        
sol = Solution()
print(sol.alien_order(words = ["wrt","wrf","er","ett","rftt"]))
print(sol.alien_order(words = ["z","x"]))
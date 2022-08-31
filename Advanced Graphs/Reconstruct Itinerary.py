import collections
from typing import List


class Solution:
    # DFS solution.
    # Use dictionary to assign an index to each airport which act as the start of a flight,
    # For each starting airpor, make a dictionary counting flights to destination airports.
    # Do a DFS decrementing the number of tickets until a valid itenerary is formes.
    # This produces valid iteneraries, but for some reason, there is a test case on leetcode
    # that does not pass because the lexical order is wrong. I don't understand why though,
    # because it seems like "JFKKULJFKNRT" should have lower lexical order than "JFKNRTJFKKUL".
    # Maybe I am misunderstanding what they mean by "lexical order when read as a single string".
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        starts = set([x[0] for x in tickets])
        ticketCount = [collections.defaultdict(int) for _ in range(len(starts))]
        startIdx = collections.defaultdict(int)
        for i, s in enumerate(starts):
            startIdx[s] = i


        for i, f in enumerate(tickets):
            ticketCount[startIdx[f[0]]][f[1]] += 1

        res = []
        itenerary = []
        def dfs(start):
            
            if len(itenerary) == len(tickets) + 1:
                if not res:
                    res.append(itenerary.copy())
                else:
                    if "".join(itenerary) < "".join(res[0]):
                        res[0] = itenerary.copy()
                return

            destinations = ticketCount[startIdx[start]].keys()
            for dest in destinations:
                if ticketCount[startIdx[start]][dest] > 0:
                    ticketCount[startIdx[start]][dest] -= 1
                    itenerary.append(dest)
                    dfs(dest)
                    ticketCount[startIdx[start]][dest] += 1
                    itenerary.pop()

        itenerary.append("JFK")
        dfs("JFK")

        return res[0]

    # Neetcode solution.
    # Create adjacency list in the form of dictionary of queues.
    # DFS works very similarly to my own solution, but uses the queues
    # instead of counting tickets.
    # If there are repeated flights, they become multiple instances of the
    # airport in the queue of adjacencies.
    # I am actually not sure if there are any test cases with repeated flights,
    # the constraints do not mention anything about it. I just assumed that this
    # was something that could happen.
    #
    # This solution takes care of the lexical ordering by sorting
    # all the tickets before creating the adjacency list, and the form
    # of the adjecncy list preserves the ordering.
    # This has the additional advantage that the algorithm can stop after
    # finding the first valid itenerary as that has the lowest lexical ordering.
    def findItinerarySorted(self, tickets: List[List[str]]) -> List[str]:
        adj = {u: collections.deque() for u, v in tickets}
        res = ["JFK"]

        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)

        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False

            temp = list(adj[cur])
            for v in temp:
                adj[cur].popleft()
                res.append(v)
                if dfs(v):
                    return res
                res.pop()
                adj[cur].append(v)
            return False

        dfs("JFK")
        return res


test = ["JFKKULJFKNRT", "JFKNRTJFKKUL"]
test.sort()
print(test)
print("")

sol = Solution()
print(sol.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(sol.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(sol.findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print("")
print(sol.findItinerarySorted(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(sol.findItinerarySorted(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(sol.findItinerarySorted(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
from typing import List

class Solution:
    # Solution using Bellman-Ford shortest path algorithm.
    # Using Dijkstra runs into complications because a vertex might be visited from a path
    # that will later turn out to be too long to be legal.
    # The BF algorithm allows us to calculate the shortest path in n edges.
    # n = stops + 1
    # 
    # Create array of price to reach vertices initialized to inf, except the source which is 0.
    # n times:
    # Make copy of array, and for all edges from x to y, check if the price of x + V_xy is less than
    # the previous cost of going to y. If so, make that the cost of going to y in copy.
    # Then overwrite the array with the copy.
    # After n iterations, we have found the price of reaching each vertex in n edges.
    # If a vertex is not reachable in n edges, the price is infinity.
    #
    # O(E * n) time.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")
        prices = [inf]*n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # source, destination, price
                if prices[s] == inf:
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == inf else prices[dst]

sol = Solution()
print(sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))
print(sol.findCheapestPrice(n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1))
print(sol.findCheapestPrice(n = 11, flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]], src = 0, dst = 2, k = 4))
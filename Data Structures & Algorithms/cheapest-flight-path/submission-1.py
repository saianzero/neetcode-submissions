class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        res = [float("inf")] * n
        res[src] = 0

        # k stops = k + 1 edges
        for i in range(k + 1):
            temp = res.copy()

            for u, v, w in flights:
                if res[u] != float("inf") and res[u] + w < temp[v]:
                    temp[v] = res[u] + w

            res = temp

        return -1 if res[dst] == float("inf") else res[dst]
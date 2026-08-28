class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        visited = set()

        min_heap = [[0,0]]

        while min_heap:

            cost, u = heapq.heappop(min_heap)

            if u in visited:
                continue
                
            visited.add(u)

            res+=cost

            x1,y1 = points[u]

            for v in range(len(points)):
                if v not in visited:
                    x2,y2 = points[v]

                    cost = abs(x1-x2) + abs(y1-y2)

                    heapq.heappush(min_heap, [cost, v])
        
        return res


        
        



            
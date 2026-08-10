class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(min_heap, (dist, p))

        
        res = []                
        while k > 0:
            d, p = heapq.heappop(min_heap)
            res.append(p)
            k-=1
        
        return res






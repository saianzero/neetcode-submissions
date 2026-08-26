class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        n = len(heights)
        m = len(heights[0])

        res = [[float("inf")]*m for _ in range(n)]
        res[0][0] = 0

        min_heap = [[0,0,0]]

        directions = [(0,-1), (-1,0), (0,1), (1,0)]

        while min_heap:

            d,x,y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx = x+dx
                ny = y+dy
            
                if 0<=nx<n and 0<=ny<m:
                    abs_diff = abs(heights[x][y] - heights[nx][ny])
                    max_diff = max(d, abs_diff)

                    if res[nx][ny] > max_diff:
                        res[nx][ny] = max_diff

                        heapq.heappush(min_heap, [res[nx][ny], nx, ny])

        return res[n-1][m-1]

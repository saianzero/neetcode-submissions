class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 0 or m == 0 or grid[0][0] == 1:
            return -1
        
        res = [[float("inf")]*m for _ in range(n)]

        res[0][0] = 0

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        min_heap = [[0,0,0]]

        while min_heap:

            d,x,y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and d+1 < res[nx][ny]:
                    res[nx][ny] = d+1
                    heapq.heappush(min_heap, [res[nx][ny],nx,ny])

                    grid[nx][ny] = 1
        if res[n-1][m-1] == float("inf"):
            return -1

        return res[n-1][m-1]+1
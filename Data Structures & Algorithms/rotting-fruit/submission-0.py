from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        fresh_count = 0

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh_count+=1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        while q:

            for _ in range(len(q)):
                i,j = q.popleft()

                for dir in dirs:
                    ni = i + dir[0]
                    nj = j + dir[1]

                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append([ni,nj])
                        fresh_count -= 1
            minutes+=1
        
        return minutes-1 if fresh_count == 0 else -1















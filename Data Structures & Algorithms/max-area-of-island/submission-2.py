class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        q = deque()
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        res = 0
        for i in range(n):
            for j in range(m):
                area = 0
                if (i,j) not in visited and grid[i][j] == 1:
                    q.append([i,j])
                    visited.add((i,j))
                
                while q:
                    x, y = q.popleft()
                    area+=1
                    for dx, dy in dirs:
                        nx = x+dx
                        ny = y+dy

                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            q.append([nx,ny])
                res = max(res, area)

        return res
 
        
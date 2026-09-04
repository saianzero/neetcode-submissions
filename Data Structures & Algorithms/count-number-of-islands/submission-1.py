class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        self.count = 0
        q = deque()
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    q.append([i,j])
                    visited.add((i,j))

                    while q: 
                        x, y = q.popleft()

                        for dx,dy in dirs:
                            nx = x + dx
                            ny = y + dy

                            if (0 <= nx < n and 
                                0<= ny < m and 
                                grid[nx][ny] == "1" and
                                (nx,ny) not in visited):

                                visited.add((nx,ny))
                                q.append([nx,ny])

                    self.count+=1
        return self.count


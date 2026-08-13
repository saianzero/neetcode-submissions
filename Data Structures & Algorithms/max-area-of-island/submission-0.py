class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen =  set()
        max_area = 0
        def dfs(r,c):

            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0 or (r,c) in seen:
                return 0
            

            seen.add((r,c))

            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    curr_area = dfs(r,c)
                    max_area = max(max_area, curr_area)
        return max_area

                




            

    


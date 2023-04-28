class Solution(object):
    def numIslands(self, grid):
        
        # 1 - land 
        # 0 - water 
        # DFS
        # every time the land found --> run the DFS 
        
        islands = 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        
        def check_correct_move(x,y):
            if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y]=='1' and (x,y) not in visited:
                return True
            else:
                return False
        def dfs(r,c):
            for new_row, new_col in [(r, c+1), (r, c-1),(r+1,c),(r-1,c)]:
                if check_correct_move(new_row,new_col):
                    visited.add((new_row,new_col))
                    dfs(new_row,new_col)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1' and (i,j) not in visited:
                    islands +=1
                    visited.add((i,j))
                    dfs(i,j)
        return islands
                    
                    
        
        
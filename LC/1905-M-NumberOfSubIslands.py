class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        islands = 0
        
        #remove any uncommon islands
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    self.dfs(row, col, grid2)
         
        #count related sub islands
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1:
                    self.dfs(row, col, grid2)
                    islands += 1
                    
        return islands
    
    def dfs(self, row, col, grid):
        
        if (row < 0) or (col < 0) or (row >= len(grid)) or (col >= len(grid[0])) or (grid[row][col] == 0):
            return
        
        grid[row][col] = 0
        
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    perimeter = self.calcPerimeter(row, col, grid)
                    break
        
        return perimeter
                    
    def calcPerimeter(self, row, col, grid):
        
        # out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 1
        
        # already traversed
        if grid[row][col] == 2:
            return 0
        
        # encountered water
        elif grid[row][col] == 0:
            return 1
        
        # set as traversed
        grid[row][col] = 2
                
        # travel
        up = self.calcPerimeter(row - 1, col, grid)
        down = self.calcPerimeter(row + 1, col, grid)
        left = self.calcPerimeter(row, col - 1, grid)
        right = self.calcPerimeter(row, col + 1 , grid)
        
        return up + down + left + right
    
class Solution:
    def getSum(self, grid, left, right, down, begin):
        result = 0
        expand = True
        
        # starting index
        cl = cr = (left + right) // 2
        
        for row in range(begin, down + 1):
            # same spot, add 1 value
            if cl == cr:
                result += grid[row][cl]
            # 2 diff indecies = 2 values
            else:
                result += grid[row][cl] + grid[row][cr]
                
            # reach edge
            if cl == left:
                expand = False
            
            if expand:
                cl -= 1
                cr += 1
            else:
                cl += 1
                cr -= 1
                
        return result
    
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                left = right = j
                down = i
                while left >= 0 and right <= n-1 and down <= m-1:
                    curr_sum = self.getSum(grid, left, right, down, i)
                    left -= 1
                    right += 1
                    down += 2
                    sums.add(curr_sum)

        sums = list(sums)
        sums.sort(reverse=True)
        return sums[:3] if len(sums) >= 3 else sums
        
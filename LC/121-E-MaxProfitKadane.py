import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv, minv = 0, sys.maxsize
        
        for i in prices:
            minv = min(i, minv)
            maxv = max(maxv, i - minv)
        
        return maxv
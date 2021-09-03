class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for acc in accounts:
            currsum = sum(acc)
            if currsum > max:
                max = currsum
        return max

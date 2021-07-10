class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = []
        for i in A:
            l.append(i*i)
        return sorted(l)
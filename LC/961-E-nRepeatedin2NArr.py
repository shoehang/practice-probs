class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in A:
            if A.count(i) == len(A)/2:
                return i
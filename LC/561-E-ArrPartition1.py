class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        newl = sorted(nums)
        value = 0
        for i in range(0,len(newl),2):
            value += min(newl[i],newl[i+1])
        return value
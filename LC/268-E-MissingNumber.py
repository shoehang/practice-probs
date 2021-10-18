class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #summation formula
        n = len(nums)
        num_sum = int((n / 2) * (n + 1))
        for num in nums:
            num_sum -= num
            
        return num_sum
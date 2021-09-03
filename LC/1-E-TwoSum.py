class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hash:
                return [i, hash[remainder]]
            else:
                hash[nums[i]] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                if dict[comp] != i:
                    return [i,dict[comp]]
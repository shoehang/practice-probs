class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            prev += curr
            nums[i] = prev
        return nums
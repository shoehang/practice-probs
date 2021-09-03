class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_arr = [None] * len(nums)
        
        left, right = 0, len(nums) - 1
        
        for index in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                sorted_arr[index] = nums[left] ** 2
                left += 1
            else:
                sorted_arr[index] = nums[right] ** 2
                right -= 1
        return sorted_arr
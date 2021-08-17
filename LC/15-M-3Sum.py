class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = N -1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
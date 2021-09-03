class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        curr_majority = nums[0]
        
        majority_count = 1
        
        for i in range(1,len(nums)):
            if majority_count == 0:
                majority_count += 1
                curr_majority = nums[i]
            elif nums[i] == curr_majority:
                majority_count += 1
            else:
                majority_count -= 1
            
        return curr_majority
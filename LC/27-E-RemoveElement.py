class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s, e  = 0, len(nums)-1
        
        while s <= e:
            if nums[s] == val:
                nums[s], nums[e], e = nums[e], nums[s], e-1
                continue
            s+=1
        return s
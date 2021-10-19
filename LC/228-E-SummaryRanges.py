class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []
        
        res, lo, hi = [], 0, 0
        
        while hi < len(nums) - 1:
            if nums[hi] + 1 != nums[hi + 1]:
                if nums[lo] == nums[hi]:
                    res.append("{}".format(nums[hi]))
                    lo = hi + 1
                else:
                    res.append("{}->{}".format(nums[lo], nums[hi]))
                    lo = hi + 1
            hi += 1
        
        if lo == hi:
            res.append("{}".format(nums[hi]))
        else:
            res.append("{}->{}".format(nums[lo], nums[hi]))
        
        return res
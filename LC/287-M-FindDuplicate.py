class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hi, lo = len(nums)-1, 0
        
        while lo < hi:
            
            mid = lo + (hi - lo) // 2
            
            count = 0
            
            for num in nums:
                if num <= mid:
                    print(num)
                    count += 1
            
            if count > mid:
                hi = mid

            else:
                lo = mid + 1
                
        return lo
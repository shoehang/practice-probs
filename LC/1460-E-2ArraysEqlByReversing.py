#using array reversal, determine if 2 arrays (target and arr) are equal if arr can swap aroound elements

#this essentially means that these arrays will have same elements/count
#no need to use swap logic

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n = len(target)
        
        if n == 1:
            if target[0] == arr[0]:
                return True
        
        counter = {}
        
        for int in target:
            if int in counter:
                counter[int] += 1
            else:
                counter[int] = 1
            
        for int in arr:
            if int in counter:
                counter[int] -= 1
                if counter[int] < 0:
                    return False
            else:
                return False
        
        return True
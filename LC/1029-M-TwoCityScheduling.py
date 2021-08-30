class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #send everyone to first city
        f = [x for x,y in costs]
        
        #get all differences for half
        d = [y - x for x,y in costs]
        half = len(costs) // 2
        d.sort()
        
        return sum(f) + sum(d[:half])
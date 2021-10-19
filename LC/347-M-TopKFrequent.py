class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        # O(n)
        for num in nums:
            if num in freq:
                freq[num] -= 1
            else:
                freq[num] = -1
                
        h = []
        
        # O(n)
        for item in freq.items():
            key, frequency = item
            heapq.heappush(h, (frequency, key))
        
        result = []
        pops = 0
        while pops < k:
            frequency, key = heapq.heappop(h)
            result.append(key)
            pops += 1
        
        
        # heap pop and push O(logk)
        return result
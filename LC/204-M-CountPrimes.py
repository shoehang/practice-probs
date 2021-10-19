class Solution:
    def countPrimes(self, n: int) -> int:
        
        if  n < 3:
            return 0
        
        # brute force is very shitty use arithmetic
        
        cache = [1] * n
        
        cache[0], cache[1] = 0, 0
        
        # O(n)
        for num in range(2, n):
            
            if cache[num] == 1:
                # O(logn) ??log(log(n))
                for non_prime in range(num ** 2, n, num):
                    cache[non_prime] = 0
        
        # O(n)
        return sum(cache)
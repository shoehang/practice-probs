class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        if N == 0:
            return 0
        elif N == 1 or N == 2:
            return 1
        elif N in memo:
            return memo[N]
        else:
            memo[N] = (self.fib(N-1) + self.fib(N-2))
            return memo[N]


#can do O(n) solution by iteration
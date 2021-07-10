class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x ^ y))[2:].count('1')
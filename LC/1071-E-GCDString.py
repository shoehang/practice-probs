import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        while True:
            
            if str1 + str2 != str2 + str1:
                return ""
            
            if str1 == str2:
                return str1
            
            length_gcd = math.gcd(len(str1), len(str2))
            
            str1 = str1[:length_gcd]
            str2 = str2[:length_gcd]
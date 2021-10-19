class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        S = s.upper().replace('-', '')
        
        res = []
        
        leftover = len(S) % k
        
        if leftover:
            res.append(S[0:leftover])
            
        for i in range(leftover, len(S), k):
            res.append(S[i:i+k])
        
        return '-'.join(res)
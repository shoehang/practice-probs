class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r, res = n, n, []
        if not n:
            return []
        self.dfs(l, r, res, "")
        return res
        
    def dfs(self, l, r, res, currstr):
        #backtrack
        if l > r or l < 0 or r < 0:
            return
        #found solution
        if l == 0 and r == 0:
            res.append(currstr)
            return
        self.dfs(l-1, r, res, currstr + "(")
        self.dfs(l, r-1, res, currstr + ")")
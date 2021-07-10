class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        newstr = ''
        currstr = ''
        pvalue = 0
        for i in S:
            currstr += i
            if i == '(':
                pvalue += 1
            if i == ')':
                pvalue -= 1
            if pvalue == 0:
                currstr = currstr[1:-1]
                newstr += currstr
                currstr = ''
        return newstr
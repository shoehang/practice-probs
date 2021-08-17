class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")":"(",
             "}":"{",
             "]":"["
            }
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d:
                try:
                    if stack.pop() != d[i]:
                        return False
                except:
                    return False
        return stack == []
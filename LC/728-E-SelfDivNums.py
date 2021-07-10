class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right+1):
            if len(str(i)) == 1:
                l.append(i)
            elif '0' in str(i):
                continue
            else:
                div = True
                for j in str(i):
                    if i%int(j) == 0:
                        continue
                    else:
                        div = False
                if div:
                    l.append(i)
        return l
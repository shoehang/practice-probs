class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xaxis = set()
        for i in range(len(points)):
            xaxis.add((points[i])[0])
        if len(xaxis) == 1:
            return 0
        sortedl = list(xaxis)
        sortedl.sort()
        widest = 1
        curr = sortedl[0]
        for i in sortedl:
            if i - curr > widest:
                widest = i - curr
            curr = i
        return widest
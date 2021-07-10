class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [0,0]
        for i in moves:
            if i == 'U':
                origin[1] += 1
            elif i == 'D':
                origin[1] -= 1
            elif i == 'L':
                origin[0] -= 1
            elif i == 'R':
                origin[0] += 1
        return origin == [0,0]
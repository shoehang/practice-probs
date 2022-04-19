class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        length = 0
        for i in range(l-1, -1, -1):
            if length == 0 and s[i] == " ":
                continue
            elif s[i] != " ":
                length += 1
            else:
                break
        return length
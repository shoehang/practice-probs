class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels=0
        for i in S:
            if i in J:
                jewels += 1
        return jewels
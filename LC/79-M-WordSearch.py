class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if self.dfs(x, y, board, word):
                    return True
        return False
    
    def dfs(self, x, y, board, word):
        if len(word) == 0:
            return True
        
        if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board) or word[0] != board[y][x]:
            return False
        
        board[y][x] = '!'
        res = \
            self.dfs(x-1, y, board, word[1:]) or \
            self.dfs(x+1, y, board, word[1:]) or \
            self.dfs(x, y-1, board, word[1:]) or \
            self.dfs(x, y+1, board, word[1:])
        board[y][x] = word[0]
        
        return res
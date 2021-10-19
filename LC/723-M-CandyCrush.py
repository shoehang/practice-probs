class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n, m = len(board), len(board[0])
        keep_crushing = False
        
        for i in range(n):
            # needs at least 2 on right horizontal crushing
            for j in range(m - 2):
                if board[i][j] == 0:
                    continue
                temp = abs(board[i][j])
                if temp == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -temp
                    keep_crushing = True
        
        # needs at least 2 on bottom vertical crushing
        for i in range(n - 2):
            for j in range(m):
                if board[i][j] == 0:
                    continue
                temp = abs(board[i][j])
                if temp == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -temp
                    keep_crushing = True
        
        if keep_crushing:
            for i in range(m):
                drop_indx = n - 1               
                for j in range(n - 1, -1, -1):
                    if board[j][i] > 0:
                        board[drop_indx][i] = board[j][i]
                        drop_indx -= 1
                while drop_indx >= 0:
                    board[drop_indx][i] = 0
                    drop_indx -= 1
        
        return self.candyCrush(board) if keep_crushing else board
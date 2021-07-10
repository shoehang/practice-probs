board = [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
	for y in range(len(board)):
		for x in range(len(board[y])):
			currVal = board[y][x]
			if currVal == ".":
				continue
			if not inBox(x, y, currVal, board) and not inRow(x, y, currVal, board) and not inCol(x, y, currVal, board) and not inBox(x, y, currVal, board):
				continue
			return False
	return True

def inRow(x, y, target, board):
	for i in range(9):
		if i == x:
			continue
		currVal = board[y][i]
		if (currVal == target):
			return True
	return False

def inCol(x, y, target, board):
	for i in range(9):
		if i == y:
			continue
		currVal = board[i][x]
		if (currVal == target):
			return True
	return False

def inBox(x, y, target, board):
	newx = x - x%3
	newy = y - y%3
	for i in range(3):
		for j in range(3):
			if i+newy == y and j+newx == x:
				continue
			currVal = board[i+newy][j+newx]
			if currVal == target:
				return True
	return False

print(isValidSudoku(board))

# https://leetcode.com/problems/valid-sudoku/discuss/355779/Python-solution-using-set-76ms
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        dices = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == '.': continue
                if e in rows[i] or e in cols[j] or e in dices[i//3][j//3]: return False
                rows[i].add(e)
                cols[j].add(e)
                dices[i//3][j//3].add(e)
        return True
'''
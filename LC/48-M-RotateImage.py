class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # first reverse the matrix
        # matrix.reverse could work here for o(n) but slight better is o(n/2)
        begin, end = 0, len(matrix) - 1
        
        while begin < end:
            matrix[begin], matrix[end] = matrix[end], matrix[begin]
            begin += 1
            end -= 1
        
        # then turn column into rows and vice versa
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
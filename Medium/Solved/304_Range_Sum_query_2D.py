class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.partialSum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        self.partialSum[0][0] = matrix[0][0]

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(1, rows):
            self.partialSum[r][0] = matrix[r][0] + self.partialSum[r-1][0]
        
        for c in range(1, cols):
            self.partialSum[0][c] = matrix[0][c] + self.partialSum[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                self.partialSum[r][c] = matrix[r][c] + self.partialSum[r][c-1] + self.partialSum[r-1][c] - self.partialSum[r-1][c-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.partialSum[row2][col2] - (self.partialSum[row2][col1-1] + self.partialSum[row1-1][col2]) + self.partialSum[row1-1][col1-1]
    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

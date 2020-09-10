class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def solve(self):
        row, col = self.find_empty()
        if row == -1 or col == -1:
            return True
        for number in range(1, 10):
            if self.isValid(row, col, str(number)):
                self.board[row][col] = str(number)
                if self.solve():
                    return True
                self.board[row][col]= "."
                
        
    def find_empty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == ".":
                    return (row, col) # row, col
        return (-1, -1)
    
    def isValid(self, row, column, number):
        if self.isRowValid(row, number) and self.isColumnValid(column, number) and self.isSubgridValid(row, column, number):
            return True
        else:
            return False
    
    def isRowValid(self, row, number):
        if str(number) in self.board[row]:
            return False
        else:
            return True
        
    def isColumnValid(self, column, number):
        if str(number) in [row[column] for row in self.board]:
            return False
        else:
            return True
        
    def isSubgridValid(self, row, column, number):
        startRow, startCol = (row//3)*3, (column//3)*3
        if str(number) in [self.board[i][j] for i in range(startRow, startRow+3) for j in range(startCol, startCol+3)]:
            return False
        else:
            return True
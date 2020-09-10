class Sudoku:
    def __init__(self, board):
        self.board = board
        
    def solve(self):
        row, col = self.find_empty()
        if row == -1 or col == -1:
            return True
        for number in range(1, 10):
            if self.isValid(row, col, number):
                self.board[row][col] = number
                if self.solve():
                    return True
                self.board[row][col]= 0
                
    def find_empty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)
        return (-1, -1)
    
    def isValid(self, row, column, number):
        if self.isRowValid(row, number) and self.isColumnValid(column, number) and self.isSubgridValid(row, column, number):
            return True
        else:
            return False
    
    def isRowValid(self, row, number):
        if number in self.board[row]:
            return False
        else:
            return True
        
    def isColumnValid(self, column, number):
        if number in [row[column] for row in self.board]:
            return False
        else:
            return True
        
    def isSubgridValid(self, row, column, number):
        startRow, startCol = (row//3)*3, (column//3)*3
        if number in [self.board[i][j] for i in range(startRow, startRow+3) for j in range(startCol, startCol+3)]:
            return False
        else:
            return True

print("Enter your sudoku board as a two dimensional lists:")

board = []
while True:
    row = list(input().split())
    if row:
        board.append([int(x) for x in row])
    else:
        break

sudoku = Sudoku(board)
sudoku.solve()
print("This is your solved sudoku board:")

for row in sudoku.board:
    print(row)
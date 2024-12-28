# Recursive backtracking solution
# TC: O(9(N^2))
# SC: O(n^2)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    def solve(self,board:List[List[str]]):
        for row in range(9):
            for col in range(9):
                if board[row][col]=='.':
                    # if place is empty then try to fill it
                    for d in range(1,10):
                        digit=str(d)
                        # check if the number can be placed
                        if self.valid(row,col,digit,board):
                            # update the value in board to digit
                            board[row][col]=digit
                            # continue to solve for other places
                            if self.solve(board):
                                return True
                        # backtrack and make this position empty
                        board[row][col]='.'
                    return False
        return True
    
    def valid(self,row,col:int,digit:str,board:List[List[str]])->bool:
        for index in range(9):
            # check row
            if board[row][index]==digit:
                return False
            # check col
            if board[index][col]==digit:
                return False
            # check sub 3*3 box
            if board[3*(row//3)+index//3][3*(col//3)+index%3]==digit:
                return False
        return True
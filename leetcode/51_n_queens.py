# Recursive back tracking solution
#  TC: O(n!)
# SC: O(n^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        boards=[]
        self.place_queen(n,0,board,boards)
        return boards
    def place_queen(self,n,col:int,board,boards:List[List[str]]):
        if col==n:
            boards.append([''.join(row) for row in board])
            return
        for row in range(n):
            if self.can_place(row,col,n,board):
                board[row][col]='Q'
                self.place_queen(n,col+1,board,boards)
                board[row][col]='.'
    
    def can_place(self,row,col,n:int,board:List[List[str]])->bool:
        # check ← left horizontal
        for c in range(col):
            if board[row][c]=='Q':
                return False
        
        # check ↖ left top diagonal
        r,c=row,col
        while r>=0 and c>=0:
            if board[r][c]=='Q':
                return False
            r-=1
            c-=1
        
        # check ↙ left bottom diagonal
        r,c=row,col
        while r<n and c>=0:
            if board[r][c]=='Q':
                return False
            r+=1
            c-=1
        
        # if all safe the return True
        return True
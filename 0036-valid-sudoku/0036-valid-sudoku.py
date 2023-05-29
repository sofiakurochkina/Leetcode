class Solution(object):
    def isValidSudoku(self, board):
        
        def checking_row(board):
            for row in range(len(board)):
                arr = []
                for col in range(len(board)):
                    if board[row][col]!='.':
                        arr.append(board[row][col])
                if len(arr)!=len(set(arr)):
                    return False
            
            return True
                
        def checking_column(board):
            for col in range(len(board)):
                arr = []
                for row in range(len(board)):
                    if board[row][col]!='.':
                        arr.append(board[row][col])
                if len(arr)!=len(set(arr)):
                    return False
                
            return True

        
        def checking_sub_box(board):
            for row in (0,3,6):
                for col in (0,3,6):
                    arr = []
                    for r in range(row,row+3):
                        for c in range(col,col+3):
                            if board[r][c]!='.':
                                arr.append(board[r][c])
                    if len(arr)!=len(set(arr)):
                        return False
                    
            return True
            
        return checking_row(board) and checking_column(board) and checking_sub_box(board)
        
        
        
        
        
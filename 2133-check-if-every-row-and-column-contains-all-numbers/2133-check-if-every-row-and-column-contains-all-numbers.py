class Solution(object):
    def checkValid(self, matrix):
        
        def checking_rows(matrix):
            for row in range(len(matrix)):
                arr = []
                for col in range(len(matrix)):
                    arr.append(matrix[row][col])
                if len(arr) != len(set(arr)) != len(matrix):
                    return False
            
            return True
        
        def checking_columns(matrix):
            for col in range(len(matrix)):
                arr = []
                for row in range(len(matrix)):
                    arr.append(matrix[row][col])
                if len(arr) != len(set(arr)) != len(matrix):
                    return False
            
            return True
        
        
        return checking_rows(matrix) and checking_columns(matrix)
                    
            
        
        
        
        
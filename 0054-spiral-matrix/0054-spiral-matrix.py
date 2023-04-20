class Solution(object):
    def spiralOrder(self, matrix):
        
        result = []
        rows = len(matrix) 
        columns = len(matrix[0])
        
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            
            # from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # downwards
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row
            if up != down:
                # from right to left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column
            if left != right:
                # upwards
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
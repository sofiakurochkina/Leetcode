class Solution(object):
    def minDeletionSize(self, strs):
        
        delete_cols = 0
        
        length = len(strs[0])
        
        for col in range(length):
            for row in range(1,len(strs)):
                
                print(strs[row][col])
                
                if ord(strs[row][col]) < ord(strs[row-1][col]):
                    delete_cols +=1
                    
                    break
                
        return delete_cols
                
                
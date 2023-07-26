class Solution(object):
    def rotateString(self, s, goal):
        
        for i in range(len(s)):
            temp_left = s[0]
            print(s[1:] + temp_left)
            s = s[1:] + temp_left
            if s == goal:
                return True
        
        return False
            
            
        
        
        
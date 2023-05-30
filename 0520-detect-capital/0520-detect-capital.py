class Solution(object):
    def detectCapitalUse(self, word):
        
        large = 0
        small = 0
        
        first = False
        
        for i in range(len(word)):
            if ord('A') <= ord(word[i]) <= ord('Z'):
                if i == 0:
                    first = True
                else:
                    first = False
                large+=1
            else:
                small+=1
        
        if large == len(word) or small == len(word) or first==True:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        

        
class Solution(object):
    def isAnagram(self, s, t):

        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] +=1
            else:
                dict[letter]=1    
        
        for letter in t:
            if letter not in dict:
                return False
            else:
                dict[letter]-=1
            if dict[letter] == 0:
                dict.pop(letter)
        
        return len(dict)==0
        
        
        
        
        
        
class Solution(object):
    def mergeAlternately(self, word1, word2):
    
        
        l = 0
        merged = ''
        
        while l < len(word1) and l< len(word2):
            merged += word1[l]
            merged += word2[l]
            l+=1
        
        print(l)
        
        if l < len(word1):
            merged += word1[l:]
            
        if l < len(word2):
            merged += word2[l:]
            
        return merged
            
            
            
            
        
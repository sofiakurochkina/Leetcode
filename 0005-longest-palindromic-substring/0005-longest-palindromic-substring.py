class Solution(object):
    def longestPalindrome(self, s):
        
        res = ''
        length = 0
        
        for i in range(len(s)):
            
            # odd length
            l = i
            r = i
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if length < r-l +1:
                    res = s[l:r+1]
                    length = r-l+1
                l-=1
                r+=1
            
            # even length
            l = i
            r = i+1
            while l >=0 and r< len(s) and s[l] == s[r]:
                if length < r-l+1:
                    res = s[l:r+1]
                    length = r-l +1
                l-=1
                r+=1
                    
        return res
                
        
        
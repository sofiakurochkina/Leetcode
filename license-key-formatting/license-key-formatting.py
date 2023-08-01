class Solution(object):
    def licenseKeyFormatting(self, s, k):
        
        reversed_all = ''
        num = 0
        
        for i in reversed(range(len(s))):
            if s[i]!='-':
                num +=1
                reversed_all+=s[i]
                
            if num == k and i!=0:
                num = 0
                reversed_all+='-'
                
        print(reversed_all)
        
        new = upper(reversed_all)[::-1]
        
        if len(new)>0 and new[0]=='-':
            new = new[1:]
            
        return new

            
        
        
            

        
        
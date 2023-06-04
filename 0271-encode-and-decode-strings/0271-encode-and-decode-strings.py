class Codec:

    def encode(self, strs):
        res = ''
        for word in strs:
            res += str(len(word)) +'#' + word
        print(res)
        return res
        
    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i=j+1+length
            
        
        return res
class Solution(object):
    def numUniqueEmails(self, emails):
        
        result = set()
        
        for email in emails:
            
            for i in range(len(email)):
                
                if email[i]=='@':
                    # we came to domain
                    break
                
                elif email[i]=='.':
                    print('.')
                    email = email[:i] + email[i+1:]
                    print(email)

                
                elif email[i]=='+':
                    print('+')
                    
                    for j in range(i,len(email)):
                        if email[j]== '@':
                            email = email[:i] + email[j:]
                            print(email)
                            break
                    break
                
                
            if email not in result:
                result.add(email)
                
        print(result)
        return len(result)
            
            
        
        
        
        
        
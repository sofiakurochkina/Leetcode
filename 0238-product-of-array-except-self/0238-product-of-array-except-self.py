class Solution(object):
    def productExceptSelf(self, nums):
        
        output = [1] * len(nums)
        
        product = 1
        for i in range(len(nums)):
            output[i] *= product
            product *= nums[i]
        
        print(output)
        
        product = 1
        for i in reversed(range(len(nums))):
            output[i] *= product
            product *= nums[i]
        
        print(output)
        return(output)
            
            
        
        """ 
        
        1 1 2 6 -- pre
        
        24 12 8  6 -- post  
        
        """
        
        
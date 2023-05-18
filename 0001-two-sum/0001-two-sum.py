class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        
        for index,num in enumerate(nums):
            if num in dict:
                return [index,dict[num]]
            else:
                dict[target-num]=index
                
        
        
        
        

        
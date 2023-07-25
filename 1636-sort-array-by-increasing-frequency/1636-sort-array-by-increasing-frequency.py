class Solution(object):
    def frequencySort(self, nums):
        
        di = Counter(nums)
        print(di)
        
        arr = sorted(di.items(),key = lambda x : (x[1],-x[0]))
        print(arr)
        
        res = []
        
        for key,val in arr:
            res += [key] * val
        
        return res
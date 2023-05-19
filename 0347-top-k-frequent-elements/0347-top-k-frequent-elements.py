class Solution(object):
    def topKFrequent(self, nums, k):
        
        if k == len(nums):
            return nums
        
        hashMap = Counter(nums)
        
        return heapq.nlargest(k,hashMap.keys(),key=hashMap.get)
        
        
        
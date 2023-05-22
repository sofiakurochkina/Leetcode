class Solution(object):
    def topKFrequent(self, nums, k):
        
        # we need to bring the most frequent element to the top of the minHeap
        
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]-=1
            else:
                dict[num]=-1
        
        h = []
        for key in dict:
            heapq.heappush(h,(dict[key], key )) # values first, then keys
        
        print(h)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(h)[1])
        
        return result
    
        
     
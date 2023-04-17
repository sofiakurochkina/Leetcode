class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums or len(nums)==1:
            return nums
        
        prefix = [1]
        postfix = [1]

        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i-1])
            postfix.append(postfix[i-1]*nums[len(nums)-i])
        
        postfix = postfix[::-1]

        print(prefix)
        print(postfix)

        return [prefix[i]*postfix[i] for i in range(len(nums))]

        
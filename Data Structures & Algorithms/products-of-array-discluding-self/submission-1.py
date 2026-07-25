class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        # traverse through the array
        # 1. store in res[i], 2. Update prefix using nums[i]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # traverse reverse through the array
        # 1. store in res[i], 2. Update postfix using nums[i]
        postfix =  1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix #multiply prefix*postfix
            postfix *= nums[i]
        
        return res

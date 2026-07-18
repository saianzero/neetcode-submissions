class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        res = float("inf")
        sum = 0
        while r < len(nums):
            sum+=nums[r]
            while sum >= target:
                sum-=nums[l]
                res = min(r-l+1, res)
                l+=1
            r+=1
        return 0 if res == float("inf") else res


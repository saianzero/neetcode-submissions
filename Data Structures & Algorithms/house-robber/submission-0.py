class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)

        def solve(nums, i):

            if i >= len(nums):
                return 0
            
            if dp[i] != -1:
                return dp[i]

            #include
            rob = nums[i] + solve(nums, i+2)

            #exclude
            skip = solve(nums, i+1)

            dp[i] = max(rob, skip)
            return dp[i]
        return solve(nums, 0)
        
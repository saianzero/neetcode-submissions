class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float("-inf")
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]
            # start = i
            if curr_sum > max_sum:
                max_sum = curr_sum
                # start_idx = start
                # end_idx = i

            if curr_sum < 0:
                curr_sum = 0

        return max_sum 
        
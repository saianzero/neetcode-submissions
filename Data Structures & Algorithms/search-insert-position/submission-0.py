class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>=target:
                res = mid
                right = mid -1
            else:
                left = mid+1
        return res

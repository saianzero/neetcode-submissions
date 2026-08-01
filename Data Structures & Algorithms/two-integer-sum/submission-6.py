class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

       
        for i, num in enumerate(nums):
            compl = target - num

            if compl in res and res[compl]!=i:
                return [res[compl], i]
            res[num] = i



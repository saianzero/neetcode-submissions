class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, el in enumerate(nums):
        
            compl = target - el
            if compl in res:
                return [res[compl], i]
            res[el] = i
            
        
        


        
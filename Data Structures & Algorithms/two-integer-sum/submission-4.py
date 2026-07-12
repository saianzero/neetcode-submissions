class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, el in enumerate(nums):
        
            compl = target - el
            if compl in res and res[compl] !=i:
                return [res[compl], i]
            res[el] = i
            
        
        


        
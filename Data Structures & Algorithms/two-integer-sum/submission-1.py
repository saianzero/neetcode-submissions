class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, el in enumerate(nums):
            res[el] = i
        
        for i, el in enumerate(nums):
            compl = target - el
            if compl in res and res[compl] !=i:
                return [i, res[compl]]
        return []
        


        
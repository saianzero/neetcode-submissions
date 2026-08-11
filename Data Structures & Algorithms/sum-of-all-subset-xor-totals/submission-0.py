class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, total):
            if i == len(nums):
                return total
            
            withN = dfs(i+1, total^nums[i])
            withoN = dfs(i+1, total)

            return withN + withoN
        
        return dfs(0,0)



        
        
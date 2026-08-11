class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = set()

        def dfs(i):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            in_level =  set()
            for i in range(len(nums)):
                if i in seen:
                    continue
                if nums[i] in in_level:
                    continue
                
                curr.append(nums[i])
                seen.add(i)
                in_level.add(nums[i])


                dfs(i+1)

                curr.pop()
                seen.remove(i)
            
        dfs(0)
        return res
        
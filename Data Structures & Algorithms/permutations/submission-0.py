class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr  = []
        seen = set()

        def dfs(i):
            
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in seen:
                    continue
                curr.append(nums[i])
                seen.add(i)

                dfs(i+1)
                
                curr.pop()
                seen.remove(i)
        
        dfs(0)
        return res
    
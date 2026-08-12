class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(oc,cc):

            if oc == cc == n:
                res.append("".join(stack))
                return
            
            if oc < n:
                stack.append("(")
                dfs(oc+1, cc)
                stack.pop()
            
            if cc < oc:
                stack.append(")")
                dfs(oc,cc+1)
                stack.pop()
        dfs(0,0)
        return res
            



                
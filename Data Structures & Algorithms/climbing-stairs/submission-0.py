class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 0:
            return 0
        if n == 0:
            return 1

        dp = [-1]*(n+1)
        return self.solve(n, dp)
    
    def solve(self, n, dp):

        if n < 0:
            return 0

        if n == 0:
            return 1

        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.solve(n-1, dp) + self.solve(n-2, dp)
        return dp[n]
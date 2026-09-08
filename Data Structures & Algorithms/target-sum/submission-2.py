class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        t = (total + target) // 2

        return self.perfectSum(nums, t)

    def perfectSum(self, arr, target):
        n = len(arr)

        t = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            t[i][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):

                if arr[i - 1] <= j:
                    t[i][j] = (
                        t[i - 1][j - arr[i - 1]]
                        + t[i - 1][j]
                    )
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][target]
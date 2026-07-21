class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = 0
        while left <= right:
            mid = (left+right)//2

            if self.get_days(weights, mid) > days:
                left=mid+1
            else:
                res = mid
                right=mid-1

        return res

    def get_days(self, weights: List[int], w: int):
        d = 1
        sum = 0
        for weight in weights:
            sum+=weight

            if sum > w:
                d+=1
                sum=weight
        return d 
                




            
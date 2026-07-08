class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        count = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num]= 1

        for n,f in freq.items():
            count[f].append(n)

        res = []
        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
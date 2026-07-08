class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
               freq[num] = 1


        res = []

        for i in range(k):
            max_num = None
            max_freq = -1

            for num in freq:
                if freq[num] > max_freq:
                    max_freq = freq[num]
                    max_num = num
            
            res.append(max_num)
            del freq[max_num]
        
        return res
        
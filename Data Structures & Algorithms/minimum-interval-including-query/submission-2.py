class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        res = {}
        # min_heap will hold (interval length, right) 
        min_heap = []
        i = 0   # represents the idx of interval in-consideration

        # process each query after sorting
        for q in sorted(queries):
            
            # Add the interval to min_heap if left <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r-l+1, r))
                i+=1
            
            # Pop all intervals that end before q, i.e right < q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # Top of the min_heap contains the smallest interval for that q
            # if min_heap is non empty, top is the answer, else -1
            res[q] = min_heap[0][0] if min_heap else -1
        
        return [res[q] for q in queries]




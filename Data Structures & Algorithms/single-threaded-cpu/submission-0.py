class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, t in enumerate(tasks):
            t.append(i)
            # [enqtime,proctime,idx]
        
        # sort based on the ascending enqueue time
        tasks.sort(key = lambda x: x[0])
        
        min_heap = []
        res = []

        #initialize time to the smallest enqueue time
        time = tasks[0][0] 
        i = 0

        # while heap or tasks still present
        while min_heap or i < len(tasks):
            # if tasks still present and available at that time, we need to add them to heap
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1],tasks[i][2]])
                i += 1

            if not min_heap:
                time=tasks[i][0]
            else:
                proc_time, idx = heapq.heappop(min_heap)
                time+=proc_time
                res.append(idx)
        return res



        



        

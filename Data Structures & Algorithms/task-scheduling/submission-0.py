class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        q = deque()  # [remaining_count, available_time]
        time = 0

        while max_heap or q:
            time += 1

            # Tasks whose cooldown is over are available now
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

            # Execute the most frequent available task
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    q.append([cnt, time + n + 1])

        return time
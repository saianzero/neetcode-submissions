class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        self.count = 0
        indegree = [0]*numCourses
        visited = set()
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        
        def bfs(numCourses):
            q = deque()
            for u in range(numCourses):
                if indegree[u] == 0:
                    q.append(u)
            while q:
                u = q.popleft()
                res.append(u)
                self.count+=1

                for v in adj[u]:
                    indegree[v]-=1
                    if indegree[v] == 0:
                        q.append(v)
            if self.count != numCourses:
                return []
            return res
        
        return bfs(numCourses)
            

            
            
        
        

        
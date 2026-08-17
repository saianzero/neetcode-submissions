class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        in_recur = set()

        adj = defaultdict(list)

        if not prerequisites:
            return True

        for u,v in prerequisites:
            adj[u].append(v)

        def dfs(u):
            visited.add(u)
            in_recur.add(u)

            for v in adj[u]:
                if v in visited and v in in_recur:
                    return False

                if v not in visited:
                    if not dfs(v):
                        return False
            in_recur.remove(u)
            return True
        
        for u in range(numCourses):
            if u not in visited:
                if not dfs(u):
                    return False
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(adj, u, visited):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(adj, v, visited)
        res = 0
        for u in range(n):
            if u not in visited:
                dfs(adj, u, visited)
                res+=1

        return res

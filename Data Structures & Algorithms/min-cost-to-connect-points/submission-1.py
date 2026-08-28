class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = list(range(len(points)))
        rank = [0]*len(points)


        def find(x):

            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):

            x_root = find(x)
            y_root = find(y)

            if x_root == y_root:
                return
            
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root]+=1




        res  = 0
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                edges.append((i, j, dist))

        
        edges = sorted(edges, key=lambda x: x[2])

        for u,v,w in edges:
            pu = find(u)
            pv = find(v)
            if pv != pu:
                union(u,v)
                res+=w
            
        return res
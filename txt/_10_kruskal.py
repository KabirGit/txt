# Kruskal's Algorithm 
class DisjointSet: 
    def __init__(self, n): 
        self.parent = list(range(n)) 
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 
    def union(self, x, y): 
        x_root = self.find(x) 
        y_root = self.find(y) 
        if x_root != y_root: 
            self.parent[x_root] = y_root 
            return True 
        return False 
def kruskal(n, edges): 
    edges.sort(key=lambda x: x[2]) 
    ds = DisjointSet(n) 
    mst = [] 
    total_weight = 0 
    for u, v, weight in edges: 
        if ds.union(u, v): 
            mst.append((u, v, weight)) 
            total_weight += weight 
 
    return mst, total_weight 
 
# Example usage: 
edges_kruskal = [ 
(0, 1, 10), 
(0, 2, 6), 
(0, 3, 5), 
(1, 3, 15), 
(2, 3, 4) 
] 
mst_k, weight_k = kruskal(4, edges_kruskal) 
print(mst_k, weight_k)
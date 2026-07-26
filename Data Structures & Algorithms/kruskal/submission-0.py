class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.size[p1] >= self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for n1, n2, w in edges:
            heapq.heappush(minHeap, (w, n1, n2))
        
        unionFind = UnionFind(n)
        res, components = 0, n
        while minHeap and components > 1:
            w, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1, n2):
                components -= 1
                res += w
    
        return res if components == 1 else -1
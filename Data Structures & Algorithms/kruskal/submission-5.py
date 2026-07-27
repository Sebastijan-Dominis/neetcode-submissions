class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
            
        if self.size[px] > self.size[py]:
            self.par[py] = px
            self.size[px] += self.size[py]
        else:
            self.par[px] = py
            self.size[py] += self.size[px]
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = [(w, v1, v2) for v1, v2, w in edges]
        heapq.heapify(heap)

        unionFind = UnionFind(n)
        components = n
        res = 0

        while heap and components > 1:
            w, s, d = heapq.heappop(heap)
            if unionFind.union(s, d):
                components -= 1
                res += w
        
        return res if components == 1 else -1
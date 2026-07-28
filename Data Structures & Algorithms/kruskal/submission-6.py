class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [0] * n
    
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key = lambda x: x[2], reverse=True)

        mst = 0
        components = n
        unionFind = UnionFind(n)

        while edges and components > 1:
            v1, v2, w = edges.pop()
            if unionFind.union(v1, v2):
                components -= 1
                mst += w
        
        return mst if components == 1 else -1
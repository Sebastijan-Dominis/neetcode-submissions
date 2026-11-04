class UnionFind:
    def __init__(self, components):
        self.components = components
        self.par = [p for p in range(components+1)]
        self.size = [1 for _ in range(components+1)]
    
    def find(self, x: int):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return False
        
        self.components -= 1
        if self.size[px] > self.size[py]:
            self.size[px] += self.size[py]
            self.par[py] = px
        else:
            self.size[py] += self.size[px]
            self.par[px] = py
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for e1, e2 in edges:
            if not unionFind.union(e1, e2):
                return [e1, e2]
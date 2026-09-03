class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)

        for e1, e2 in edges:
            unionFind.union(e1, e2)

        return unionFind.components

class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.components = n

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.size[px] >= self.size[py]:
            self.par[py] = px
            self.size[px] += self.size[py]
        else:
            self.par[px] = py
            self.size[py] += self.size[px]
        self.components -= 1
        return True
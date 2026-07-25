class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        par_x, par_y = self.find(x), self.find(y)

        if par_x == par_y:
            return False
        
        if self.size[par_x] > self.size[par_y]:
            self.par[par_y] = par_x
            self.size[par_x] += self.size[par_y]
        else:
            self.par[par_x] = par_y
            self.size[par_y] += self.size[par_x]
        self.components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.components

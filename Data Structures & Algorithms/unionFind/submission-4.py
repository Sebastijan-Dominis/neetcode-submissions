class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.components = n

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)

        if x_par == y_par:
            return False

        if self.rank[x_par] > self.rank[y_par]:
            self.par[y_par] = x_par
            self.rank[x_par] += self.rank[y_par]
        else:
            self.par[x_par] = y_par
            self.rank[y_par] += self.rank[x_par]
        self.components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.components

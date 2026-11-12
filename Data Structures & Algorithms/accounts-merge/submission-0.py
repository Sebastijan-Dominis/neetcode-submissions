class UnionFind:
    def __init__(self, components: int):
        self.components = components
        self.par = [i for i in range(components)]
        self.size = [1 for _ in range(components)]
    
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.par[x], self.par[y]

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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroups = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroups[leader].append(e)
        
        res = []
        for i, emails in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res
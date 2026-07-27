class Graph:
    
    def __init__(self):
        self.adj = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adj and dst in self.adj[src]:
            self.adj[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self.dfs(src, dst, visit)

    def dfs(self, curr: int, dst: int, visit: set) -> bool:
        if curr == dst:
            return True
        
        if curr in visit:
            return False
        
        visit.add(curr)

        for nei in self.adj.get(curr, ()):
            if nei not in visit:
                if self.dfs(nei, dst, visit):
                    return True
        
        return False
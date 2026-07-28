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

        def dfs(curr: int, dst: int) -> bool:
            if curr in visit:
                return False
            
            if curr == dst:
                return True
            
            visit.add(curr)

            for nei in self.adj.get(curr, ()):
                if nei not in visit:
                    if dfs(nei, dst):
                        return True
            
            return False
        
        return dfs(src, dst)
class Graph:
    
    def __init__(self):
        self.adj = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj[src]:
            return False
        
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)

    def dfs(self, curr: int, dst: int, visited: set) -> bool:
        if curr in visited:
            return False
        
        if curr == dst:
            return True

        visited.add(curr)

        for nei in self.adj.get(curr, ()):
            if self.dfs(nei, dst, visited):
                return True
        
        return False
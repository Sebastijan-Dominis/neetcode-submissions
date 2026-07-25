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
        visited = set()
        return self.dfs(visited, src, dst)

    def dfs(self, visited: set, curr: int, dst: int) -> bool:
        if curr in visited:
            return False
        
        if curr == dst:
            return True
        
        visited.add(curr)

        for nei in self.adj.get(curr, ()):
            if self.dfs(visited, nei, dst):
                return True
        
        return False
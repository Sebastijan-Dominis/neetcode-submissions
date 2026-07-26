class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        
        visiting, visited = set(), set()
        topSort = []

        def dfs(v: int) -> bool:
            if v in visited:
                return True
            
            if v in visiting:
                return False
            
            visiting.add(v)

            for nei in adj.get(v, ()):
                if not dfs(nei):
                    return False
            
            visiting.remove(v)
            visited.add(v)
            topSort.append(v)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        
        topSort.reverse()
        return topSort
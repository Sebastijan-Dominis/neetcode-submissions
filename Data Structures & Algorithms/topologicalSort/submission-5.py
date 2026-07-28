class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
        
        topSort = []
        visiting, visited = set(), set()

        def dfs(v):
            if v in visiting:
                return False
            
            visiting.add(v)

            for nei in adj.get(v, ()):
                if nei not in visited:
                    if not dfs(nei):
                        return False
            
            visiting.remove(v)
            visited.add(v)
            topSort.append(v)
            return True
        
        for v in range(n):
            if v not in visited:
                if not dfs(v):
                    return []
        
        topSort.reverse()
        return topSort
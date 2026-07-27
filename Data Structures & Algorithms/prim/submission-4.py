class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2, w in edges:
            adj[v1].append((v2, w))
            adj[v2].append((v1, w))
        
        heap = [(0, 0)]
        res = 0
        visit = set()

        while heap and len(visit) < n:
            w, v = heapq.heappop(heap)
            if v in visit:
                continue
            
            res += w
            visit.add(v)

            for nei, w_nei in adj.get(v, ()):
                if nei not in visit:
                    heapq.heappush(heap, (w_nei, nei))
        
        return res if len(visit) == n else -1
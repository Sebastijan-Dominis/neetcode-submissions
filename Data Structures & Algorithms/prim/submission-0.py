class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2, w in edges:
            adj[n1].append((n2, w))
            adj[n2].append((n1, w))
        
        res = 0
        visit = set()
        minHeap = [(0, 0)]

        while minHeap and len(visit) < n:
            w, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            
            visit.add(v)
            res += w

            for neighbor, weight in adj.get(v, ()):
                if neighbor not in visit:
                    heapq.heappush(minHeap, (weight, neighbor))
                
        return res if len(visit) == n else -1
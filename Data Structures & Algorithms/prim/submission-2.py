class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2, w in edges:
            adj[v1].append((v2, w))
            adj[v2].append((v1, w))

        minHeap = [(0, 0)]
        visit = set()
        res = 0
        while minHeap and len(visit) < n:
            w, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            visit.add(v)
            res += w

            for nei, w_nei in adj.get(v, ()):
                if nei not in visit:
                    heapq.heappush(minHeap, (w_nei, nei))
        
        return res if len(visit) == n else -1
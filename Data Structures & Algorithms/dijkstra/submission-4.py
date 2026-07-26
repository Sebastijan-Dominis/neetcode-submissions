class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))
        
        minHeap = [(0, src)]
        shortest = {}
        while minHeap:
            w1, d1 = heapq.heappop(minHeap)
            if d1 in shortest:
                continue
            shortest[d1] = w1

            for d2, w2 in adj.get(d1, ()):
                if d2 not in shortest:
                    heapq.heappush(minHeap, (w1+w2, d2))
                
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
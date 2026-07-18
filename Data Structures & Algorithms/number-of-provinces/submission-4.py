class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        included = [False] * N

        def dfs(start):
            stack = [start]
            included[start] = True

            while stack:
                city = stack.pop()
                for nei_city in range(N):
                    if isConnected[city][nei_city] and not included[nei_city]:
                        included[nei_city] = True
                        stack.append(nei_city)
            
        provinces = 0
        
        for city in range(N):
            if not included[city]:
                dfs(city)
                provinces += 1

        return provinces
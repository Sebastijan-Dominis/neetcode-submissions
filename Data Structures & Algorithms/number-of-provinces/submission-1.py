class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        included = [False] * N

        def dfs(start):
            stack = [start]

            while stack:
                node = stack.pop()
                for neighbor in range(N):
                    if isConnected[node][neighbor] == 1 and not included[neighbor]:
                        included[neighbor] = True
                        stack.append(neighbor)
        
        provinces = 0

        for city in range(N):
            if not included[city]:
                dfs(city)
                provinces += 1
        
        return provinces
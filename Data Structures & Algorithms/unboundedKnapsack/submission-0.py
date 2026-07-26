class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp = [0] * M

        for i in range(N):
            currRow = [0] * M
            for c in range(M):
                skip = dp[c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + currRow[c - weight[i]]
                currRow[c] = max(skip, include)
            dp = currRow
        
        return dp[M-1]
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        dp = [0] * m

        for c in range(m):
            if weight[0] <= c:
                dp[c] = profit[0]
        
        for i in range(1, n):
            curRow = [0] * m
            for c in range(1, m):
                skip = dp[c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(skip, include)
            dp = curRow
        return dp[-1]
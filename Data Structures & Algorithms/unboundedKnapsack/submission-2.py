class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        dp = [0] * m

        for i in range(n):
            curRow = [0] * m
            for c in range(m):
                skip = dp[c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + curRow[c - weight[i]]
                curRow[c] = max(skip, include)
            dp = curRow
        return dp[m-1]
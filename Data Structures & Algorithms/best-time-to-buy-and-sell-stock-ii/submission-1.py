class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            buy = prices[i-1]
            sell = prices[i]
            potential = sell - buy
            
            if potential >= 0:
                profit += potential

        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(len(prices)):
            buy = prices[l]
            sell = prices[r]
            potential = sell - buy
            
            if potential >= 0:
                profit += potential
            l = r
        
        return profit
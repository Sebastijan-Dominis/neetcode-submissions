class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float("inf")] * (amount+1)
        amounts[0] = 0

        for a in range(amount+1):
            for c in coins:
                if (a-c) >= 0:
                    amounts[a] = min(amounts[a], amounts[a-c] + 1)
        
        return amounts[-1] if amounts[-1] != float("inf") else -1
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        maxLeft, maxRight = [0] * n, [0] * n
        for i in range(1, n):
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i+1], maxRight[i+1])
        
        minimums = [min(l, r) for l, r in zip(maxLeft, maxRight)]

        for i, h in enumerate(height):
            if h < minimums[i]:
                res += (minimums[i]-h)
        
        return res
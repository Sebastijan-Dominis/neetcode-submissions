class Solution:
    def climbStairs(self, n: int) -> int:
        nextStep, stepAfterNext = 1, 1

        for i in range(n-2, -1, -1):
            temp = nextStep
            nextStep = nextStep + stepAfterNext
            stepAfterNext = temp
        
        return nextStep
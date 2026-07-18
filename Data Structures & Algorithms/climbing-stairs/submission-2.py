class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = {}

        def step(i):
            if i in memoize:
                return memoize[i]
            if i == n:
                return 1
            if i > n:
                return 0
            
            memoize[i] = step(i+1) + step(i+2)
            return memoize[i]
        
        return step(0)
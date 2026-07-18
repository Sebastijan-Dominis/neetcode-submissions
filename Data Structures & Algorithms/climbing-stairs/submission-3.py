class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = {n: 1, n-1: 1}

        for i in range(n-2, -1, -1):
            ways_to_climb[i] = ways_to_climb[i+1] + ways_to_climb[i+2]
        
        return ways_to_climb[0]
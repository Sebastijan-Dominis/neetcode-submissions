class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        n -= 1

        while n:
            temp = one
            one = one + two
            two = temp
            n -= 1
        
        return one
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countBitsInNum(i))
        return res
    def countBitsInNum(self, n):
        ones = 0
        while n:
            ones += 1
            n &= n-1
        return ones
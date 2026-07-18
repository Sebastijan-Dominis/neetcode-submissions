class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        for n in nums:
            if n != prev + 1:
                return prev + 1
            prev = n
        return prev + 1
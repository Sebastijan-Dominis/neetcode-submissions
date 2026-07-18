class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = 0
        for i in range(1, len(nums) + 1):
            expectedSum += i
        
        return expectedSum - sum(nums)
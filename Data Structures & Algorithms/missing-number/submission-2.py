class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)

        for i in range(0, len(nums) + 1):
            if i not in numbers:
                return i
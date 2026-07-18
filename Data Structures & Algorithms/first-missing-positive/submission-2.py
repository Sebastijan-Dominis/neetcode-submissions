class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        for num in range(1, len(nums)+2):
            if num not in numsSet:
                return num
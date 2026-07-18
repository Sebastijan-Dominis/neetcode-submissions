class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1

        for num in nums:
            if res == num:
                res += 1
        
        return res
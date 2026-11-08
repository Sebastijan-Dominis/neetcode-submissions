class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        res = len(nums)
        currSum = 0

        l = 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                res = min(res, r-l+1)
                currSum -= nums[l]
                l += 1
        
        return res
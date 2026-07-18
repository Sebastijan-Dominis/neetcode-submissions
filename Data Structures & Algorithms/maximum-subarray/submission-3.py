class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = nums[0], nums[0]

        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        
        return res
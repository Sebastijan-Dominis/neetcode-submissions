class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        currSum = 0
        l = 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                res = min(res, r-l+1)
                currSum -= nums[l]
                l += 1
        
        return res if res != float("inf") else 0
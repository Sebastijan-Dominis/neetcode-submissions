class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = float("-inf")

        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        
        return res
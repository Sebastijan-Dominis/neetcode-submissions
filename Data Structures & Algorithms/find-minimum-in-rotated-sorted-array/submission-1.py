class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            
            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l += 1
            else:
                r -= 1
        
        return res
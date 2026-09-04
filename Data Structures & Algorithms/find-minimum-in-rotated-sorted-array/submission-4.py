class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return min(minimum, nums[l])
            
            m = (l+r) // 2
            minimum = min(minimum, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return minimum
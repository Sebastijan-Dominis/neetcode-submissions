class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                nums.pop(r)
            l = r
            r += 1
        
        return len(nums)
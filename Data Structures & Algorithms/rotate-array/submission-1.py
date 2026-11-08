class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        tmp = [0] * len(nums)

        n = (len(nums) - k) % len(nums)
        i = 0
        while n < len(nums):
            tmp[i] = nums[n]
            n += 1
            i += 1
        
        n = 0
        while n < (len(nums) - k) % len(nums):
            tmp[i] = nums[n]
            n += 1
            i += 1
        
        for j in range(len(nums)):
            nums[j] = tmp[j]
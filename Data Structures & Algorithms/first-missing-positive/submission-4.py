class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            val = abs(num)
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1000)
        
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1

        [0,0,1,2]
        [-5,-5,1,2]
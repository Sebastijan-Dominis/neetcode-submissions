class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            val = abs(num)
            if 1 <= val <= n:
                curr = abs(nums[val-1])
                if curr > 0:
                    nums[val-1] = -1 * abs(curr)
                elif curr == 0:
                    nums[val-1] = -1 * (n+1)
        
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i
        
        return n+1

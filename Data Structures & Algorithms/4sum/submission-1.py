class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, kSum = [], []

        def helper(k: int, start: int, target: int) -> None:
            if k < 2 or k > len(nums):
                return

            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    kSum.append(nums[i])
                    helper(k-1, i+1, target - nums[i])
                    kSum.pop()
                return
            
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(kSum + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        helper(4, 0, target)
        return res
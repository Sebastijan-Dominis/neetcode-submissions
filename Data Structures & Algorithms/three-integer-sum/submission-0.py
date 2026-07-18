class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                threeSum = a + b + c

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, b, c])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res
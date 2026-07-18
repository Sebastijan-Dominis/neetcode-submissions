class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            indices[num] = i
        
        for i, num in enumerate(nums):
            missing = target - num
            if missing in indices and i != indices[missing]:
                j = indices[missing]
                return [i, j] if i < j else [j, i]
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(i for i in range(0, len(nums)+1))

        for num in nums:
            expected.remove(num)
        
        return list(expected)[0]
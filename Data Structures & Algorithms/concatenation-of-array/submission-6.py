class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for _ in range(1):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans
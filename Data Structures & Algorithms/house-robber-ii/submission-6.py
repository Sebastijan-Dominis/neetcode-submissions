class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
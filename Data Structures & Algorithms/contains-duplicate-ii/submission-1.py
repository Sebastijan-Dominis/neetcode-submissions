class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        numSet = set()

        for i in range(0, min(k+1, len(nums))):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        
        l = 0
        for r in range(k+1, len(nums)):
            numSet.remove(nums[l])
            if nums[r] in numSet:
                return True
            numSet.add(nums[r])
            l += 1
        
        return False
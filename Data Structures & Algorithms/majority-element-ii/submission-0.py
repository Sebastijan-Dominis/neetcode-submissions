class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        thresh = len(nums) // 3
        res = []

        for key, val in count.items():
            if val > thresh:
                res.append(key)
        
        return res
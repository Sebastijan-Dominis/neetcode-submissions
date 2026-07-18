class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        curr = 0
        total = 0

        for num in nums:
            prefixSum[curr] += 1
            curr += num
            total += prefixSum[curr-k]
        
        return total
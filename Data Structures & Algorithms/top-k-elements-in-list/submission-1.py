class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        freq_arr = [[freq, num] for num, freq in freq.items()]
        freq_arr.sort()

        res, remaining = [], k

        while remaining:
            res.append(freq_arr.pop()[1])
            remaining -= 1
        return res
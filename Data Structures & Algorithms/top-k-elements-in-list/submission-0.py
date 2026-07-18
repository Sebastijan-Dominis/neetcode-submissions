class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        freq_arr = [[freq, num] for num, freq in freqs.items()]
        freq_arr.sort()

        res, remaining = [], k
        while remaining:
            res.append(freq_arr.pop()[1])
            remaining -= 1
        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            newCount = defaultdict(int)

            for n, c in count.items():
                if c > 1:
                    newCount[n] = c-1
            
            count = newCount
        
        res = []

        for n in count.keys():
            c = nums.count(n)
            if c > len(nums) // 3:
                res.append(n)

        return res
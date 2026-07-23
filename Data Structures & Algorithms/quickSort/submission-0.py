# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs, l, r):
        if l >= r:
            return
        
        pivot = pairs[r]
        left = l

        for i in range(l, r):
            if pairs[i].key < pairs[r].key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
            
        pairs[r] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, l, left-1)
        self.quickSortHelper(pairs, left+1, r)
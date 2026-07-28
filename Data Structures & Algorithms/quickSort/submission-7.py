# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSortHelper(self, pairs: list[Pair], l: int, r: int):
        if l >= r:
            return
        
        left = l
        pivot = pairs[r]

        for i in range(l, r):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        
        pairs[left], pairs[r] = pivot, pairs[left]

        self.quickSortHelper(pairs, l, left-1)
        self.quickSortHelper(pairs, left+1, r)
    
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, l, m, r):
        left, right = pairs[l:m+1], pairs[m+1:r+1]
        i, j, k = l, 0, 0

        while j < len(left) and k < len(right):
            if left[j].key <= right[k].key:
                pairs[i] = left[j]
                j += 1
            else:
                pairs[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            pairs[i] = left[j]
            j += 1
            i += 1
        
        while k < len(right):
            pairs[i] = right[k]
            k += 1
            i += 1
        
        return pairs

    def sortPairs(self, pairs, l, r):
        if l >= r:
            return pairs
        
        m = (l+r) >> 1
        self.sortPairs(pairs, l, m)
        self.sortPairs(pairs, m+1, r)
        self.merge(pairs, l, m, r)
        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        return self.sortPairs(pairs, 0, len(pairs) - 1)
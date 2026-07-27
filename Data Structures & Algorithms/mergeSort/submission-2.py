# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def mergeSortHelper(self, pairs: list[Pair], l: int, r: int) -> None:
        if l >= r:
            return
        
        m = (l+r) >> 1
        self.mergeSortHelper(pairs, l, m)
        self.mergeSortHelper(pairs, m+1, r)
        self.merge(pairs, l, m, r)
    
    def merge(self, pairs: list[Pair], l: int, m: int, r: int) -> None:
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
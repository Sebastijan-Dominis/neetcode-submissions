# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, l, m, r):
        left, right = arr[l:m+1], arr[m+1:r+1]
        i, j, k = l, 0, 0

        while j < len(left) and k < len(right):
            if left[j].key <= right[k].key:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        
        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1
        
        return arr

    def mergePairs(self, arr, l, r):
        if l >= r:
            return arr
        
        m = (l+r) >> 1
        self.mergePairs(arr, l, m)
        self.mergePairs(arr, m+1, r)
        self.merge(arr, l, m, r)
        return arr

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergePairs(pairs, 0, len(pairs) - 1)

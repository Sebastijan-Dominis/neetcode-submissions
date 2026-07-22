class Solution:
    def merge(self, arr, l, m, r):
        left, right = arr[l:m+1], arr[m+1:r+1]
        i, j, k = l, 0, 0

        while j < len(left) and k < len(right):
            if left[j] < right[k]:
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

    def mergeSort(self, arr, l, r):
        if l >= r:
            return arr
        
        m = (r+l) >> 1
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m+1, r)
        self.merge(arr, l, m, r)
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
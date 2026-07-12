class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = arr[-1]
        for i in range (len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_so_far
            max_so_far = max(temp,max_so_far)
        arr[-1] = -1
        return arr

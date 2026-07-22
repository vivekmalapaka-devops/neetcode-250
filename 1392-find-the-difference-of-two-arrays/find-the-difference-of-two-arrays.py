class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = []
        arr2 = []
        for i in set(nums1):
            if i not in nums2:
                arr1.append(i)
        for j in set(nums2):
            if j not in nums1:
                arr2.append(j)
        return [arr1,arr2]
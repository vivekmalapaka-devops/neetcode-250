class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range (0,len(nums1)):
            max_1 = nums1[i]
            for j in range (nums2.index(nums1[i]),len(nums2)):
                max_2 = max(max_1,nums2[j])
                if max_2>max_1:
                    ans.append(max_2)
                    break
            if max_1==max_2:
                ans.append(-1)
        return ans
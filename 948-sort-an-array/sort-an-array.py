class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        else:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            sorted_l = self.sortArray(left)
            sorted_r = self.sortArray(right)
            return self.merge(sorted_l,sorted_r)


    def merge(self,left,right):
        l,r = 0,0
        ans = []
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                ans.append(left[l])
                l+=1
            else:
                ans.append(right[r])
                r+=1
        return ans+left[l:]+right[r:]


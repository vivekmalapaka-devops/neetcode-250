class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            if len(nums) == 1:
                return nums
            else:
                mid = len(nums)//2
                left = nums[:mid]
                right = nums[mid:]
                sorted_right = self.sortArray(right)
                sorted_left = self.sortArray(left)
                return self.merge(sorted_left, sorted_right)
    
    def merge(self,leftt,rightt):
        ans = []
        l,r = 0,0
        while l<len(leftt) and r<len(rightt):
            if leftt[l]<rightt[r]:
                ans.append(leftt[l])
                l+=1
            else:
                ans.append(rightt[r])
                r+=1
        return ans+leftt[l:]+rightt[r:]
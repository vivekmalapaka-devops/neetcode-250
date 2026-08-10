class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = True
        des = True
        for i in range (0,len(nums)-1):
            if nums[i]<nums[i+1]:
                des = False
            if nums[i]>nums[i+1]:
                asc = False

        return asc or des
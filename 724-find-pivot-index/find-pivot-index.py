class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range (0,len(nums)):
            sum_left = sum(nums[:i+1])
            sum_right = sum(nums[i:])
            if sum_left == sum_right:
                return i 
        return -1
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = sorted(nums)
        des = sorted(nums,reverse=True)
        if asc == nums or des == nums:
            return True
        return False
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_s = sorted(nums)
        n = len(nums)
        return ((sorted_s[n-1]*sorted_s[n-2])-sorted_s[1]*sorted_s[0])
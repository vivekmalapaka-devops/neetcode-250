class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > len(nums)/2:
                return i

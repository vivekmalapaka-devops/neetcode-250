class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind,val in enumerate(nums):
            complement = target - val
            if complement in d:
                return [d[complement],ind]
            d[val] = ind
        return []
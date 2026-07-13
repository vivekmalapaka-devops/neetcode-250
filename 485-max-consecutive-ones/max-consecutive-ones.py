class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0
        for i in nums:
            if i == 1:
                count+=1
                max_c = max(count,max_c)
            else:
                count=0
        return max_c
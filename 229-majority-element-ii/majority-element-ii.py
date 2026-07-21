class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        array = []
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for k,v in d.items():
            if v>len(nums)//3:
                array.append(k)
        return array
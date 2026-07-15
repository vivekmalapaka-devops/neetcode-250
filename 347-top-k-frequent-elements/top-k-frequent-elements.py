class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        
        sort_d = sorted(d.items(), key = lambda item : item[1], reverse = True)
        arr = sort_d[:k]
        result = []
        for pair in arr:
            result.append(pair[0])
        return result
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = 0
        repeated = 0 
        d = {}
        n = len(grid)**2
        nums = list(range(1, n + 1))
        for i in grid:
            for j in i:
                d[j] = d.get(j,0)+1
        for k,v in d.items():
            if v==2:
                repeated = k
        for j in nums:
            if j not in d.keys():
                missing = j
        return [repeated,missing]
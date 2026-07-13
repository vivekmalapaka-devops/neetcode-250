class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = 0
        d = {}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if k == v:
                count = max(count,k)
        if count >0:
            return count
        else:
            return -1
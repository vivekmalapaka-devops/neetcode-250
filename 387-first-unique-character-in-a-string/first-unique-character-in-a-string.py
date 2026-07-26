class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for j in s:
            if d[j]==1:
                return s.index(j)
        return -1
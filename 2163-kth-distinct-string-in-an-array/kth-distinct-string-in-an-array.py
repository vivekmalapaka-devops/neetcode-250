class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        a=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        for j in arr:
            if d[j] == 1:
                a.append(j)
        if len(a)<k:
            return ""
        else:
            return a[k-1]
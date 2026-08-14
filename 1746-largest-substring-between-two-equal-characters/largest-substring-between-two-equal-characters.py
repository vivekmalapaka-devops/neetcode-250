class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        diff = 0 
        d={}
        for i in range (0,len(s)):
            d[s[i]] = d.get(s[i],[])+[i]
        for k,v in d.items():
            if len(v)>1:
                diff_i = v[-1]-v[0]
                diff = max(diff,diff_i) 
        return (diff-1)
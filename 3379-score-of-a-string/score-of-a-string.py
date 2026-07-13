class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range (0,len(s)-1):
            abs_diff = abs((ord(s[i])-ord(s[i+1])))
            ans+=abs_diff
        return ans

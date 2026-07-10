class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)
        a,b = s[0], s[-1]
        c = ""
        for i in range (len(a)):
            if a[i]!=b[i]:
                break
            c+=a[i]
        return c
            
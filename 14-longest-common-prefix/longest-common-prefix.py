class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = ""
        sorted_s = sorted(strs)
        a = sorted_s[0]
        b = sorted_s[-1]
        for i in range (0,len(a)):
            if a[i]!=b[i]:
                break
            else:
                count+=a[i]
        return count

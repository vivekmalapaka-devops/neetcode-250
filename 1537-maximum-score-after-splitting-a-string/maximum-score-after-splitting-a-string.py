class Solution:
    def maxScore(self, s: str) -> int:
        a = []
        for i in range (1,len(s)):
            left = (s[:i])
            left_c= left.count("0")
            right = (s[i:])
            right_c = right.count("1")
            a.append(left_c+right_c)
        return max(a)
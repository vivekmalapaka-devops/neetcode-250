class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = s.rstrip()
        left = right.lstrip()
        ans = left.split(" ")
        return len(ans[-1])
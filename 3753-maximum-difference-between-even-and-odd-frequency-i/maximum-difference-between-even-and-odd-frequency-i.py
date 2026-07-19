class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
        max_odd = 0
        min_even = float('inf')
        for k,v in freq.items():
            if v%2==0:
                min_even = min(v,min_even)
            else:
                max_odd = max(v,max_odd)
        
        return (max_odd-min_even)

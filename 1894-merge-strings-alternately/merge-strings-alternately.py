class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""            
        a,b = min(len(word1),len(word2)),0
        while b<a:
            ans+=word1[b]+word2[b]
            b+=1
        return ans+word1[b:]+word2[b:]
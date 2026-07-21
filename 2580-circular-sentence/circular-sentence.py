class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(" ")
        if l[0][0] != l[-1][-1]:
            return False     
        for i in range (0,len(l)-1):
            if l[i][-1] != l[i+1][0]:
                return False
        return True
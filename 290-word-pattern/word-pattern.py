class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_ps = {}
        map_sp = {}
        s = s.split(" ")
        if len(s)!=len(pattern):
            return False
        for i in range (0,len(pattern)):
            if s[i] in map_ps and map_ps[s[i]]!=pattern[i]:
                return False
            if pattern[i] in map_sp and map_sp[pattern[i]]!=s[i]:
                return False
            map_ps[s[i]] = pattern[i] 
            map_sp[pattern[i]] = s[i]

        return True

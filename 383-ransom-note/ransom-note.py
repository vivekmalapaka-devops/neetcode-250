class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_magazine = Counter(magazine)        
        d_ransomNote = Counter(ransomNote)

        for k,v in d_ransomNote.items():
            if d_magazine[k]<v:
                return False
        return True
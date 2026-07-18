class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        ans = []
        for i in strs:
            sorted_i = sorted(i)
            string = "".join(sorted_i)
            count[string] = count.get(string,[])+[i]
        
        for k,v in count.items():
            ans.append(v)
        return ans
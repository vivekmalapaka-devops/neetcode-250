class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        ans =[]
        for i in range (len(strs)):
            sort = sorted(strs[i])
            a = "".join(sort)
            count[a] = count.get(a,[])+[strs[i]]
        for v in count.values():
            ans.append(v)
        return ans
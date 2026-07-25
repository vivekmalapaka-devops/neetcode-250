class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s_heights = sorted(heights,reverse=True)
        ans = []
        for i in s_heights:
            a = heights.index(i)
            ans.append(names[a])
        return ans
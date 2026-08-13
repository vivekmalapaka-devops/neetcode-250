class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = [[0,0]]
        for i in path:
            if i == "N":
                last = seen[-1]
                curr = [last[0],last[-1]+1]
                if curr in seen:
                    return True
                seen.append(curr)
            elif i == "E":
                last = seen[-1]
                curr = [last[0]+1,last[-1]]
                if curr in seen:
                    return True
                seen.append(curr)
            elif i == "S":
                last = seen[-1]
                curr = [last[0],last[-1]-1]
                if curr in seen:
                    return True     
                seen.append(curr)
            elif i == "W":
                last = seen[-1]
                curr = [last[0]-1,last[-1]]
                if curr in seen:
                    return True
                seen.append(curr)
        return False
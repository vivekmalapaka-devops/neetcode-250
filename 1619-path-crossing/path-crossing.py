class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = [[0, 0]]

        def is_seen(curr):
            if curr in seen:
                return True
            return False

        for i in path:
            if i == "N":
                last = seen[-1]
                curr = [last[0], last[-1] + 1]

                if is_seen(curr):
                    return True

                seen.append(curr)

            elif i == "E":
                last = seen[-1]
                curr = [last[0] + 1, last[-1]]

                if is_seen(curr):
                    return True

                seen.append(curr)

            elif i == "S":
                last = seen[-1]
                curr = [last[0], last[-1] - 1]

                if is_seen(curr):
                    return True

                seen.append(curr)

            elif i == "W":
                last = seen[-1]
                curr = [last[0] - 1, last[-1]]

                if is_seen(curr):
                    return True

                seen.append(curr)

        return False
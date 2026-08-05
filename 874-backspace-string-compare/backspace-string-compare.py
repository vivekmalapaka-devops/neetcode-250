class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ = []
        t_ = []
        for i in s:
            if i.isalpha():
                s_.append(i)
            elif i == "#" and s_:
                s_.pop()
            else:
                continue
        for i in t:
            if i.isalpha():
                t_.append(i)
            elif i == "#" and t_:
                t_.pop()
            else:
                continue
        if s_ == t_:
            return True
        else:
            return False
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = []
        for i in emails:
            email = ""
            index = i.find("@")
            domain = i[index:]
            for j in i: 
                if j == ".":
                    continue
                elif j.isalpha():
                    email+=j
                elif j == "+": 
                    break
                elif j == "@":
                    break
            email+=domain
            l.append(email)
        set_l = set(l)  
        return len(set_l)

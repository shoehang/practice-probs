class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = []
        for i in emails:
            local = ((i.split("@")[0]).split("+")[0]).replace('.','')
            domain = i.split("@")[1]
            address = local + '@' + domain
            if address not in l:
                l.append(address)
        return len(l)
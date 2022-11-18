from typing import List


class Solution:
    # Solution using hashset to find unique mails.
    # Split into local and domain part and process local part.
    # Split on "+" and use only prior part. Erase all "."s.
    # Join into full address and add to set.
    def numUniqueEmails(self, emails: List[str]) -> int:
        addresses = set()
        for add in emails:
            local, domain = add.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            addresses.add("".join([local, "@", domain]))
        return len(addresses)
    
sol = Solution()
print(sol.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(sol.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        size = [1] * n
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if size[root_x] < size[root_y]:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]
                else:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]
                    
        email_to_id = {}
        email_to_name = {}
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = i
                union(i, email_to_id[email])
                email_to_name[email] = name
                
        id_to_emails = {}
        for email, i in email_to_id.items():
            root = find(i)
            if root not in id_to_emails:
                id_to_emails[root] = []
            id_to_emails[root].append(email)
            
        res = []
        for i, emails in id_to_emails.items():
            res.append([email_to_name[emails[0]]] + sorted(emails))
        return res
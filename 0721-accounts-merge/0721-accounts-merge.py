from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)
                
        components = defaultdict(list)
        for email in parent:
            root = find(email)
            components[root].append(email)
            
        result = []
        for root, emails in components.items():
            result.append([email_to_name[root]] + sorted(emails))
            
        return result
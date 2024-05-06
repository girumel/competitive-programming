# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_to_domain = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            names = domain.split(".")

            for i in range(len(names)):
                subdomain = ".".join(names[i:])
                count_to_domain[subdomain] = count_to_domain.get(subdomain, 0) + count

        return [f"{count} {domain}" for domain, count in count_to_domain.items()]
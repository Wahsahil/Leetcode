class Solution(object):
    def subdomainVisits(self, cpdomains):

        freq = {}

        for domain in cpdomains:
            count, domain = domain.split()

            count = int(count)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])

                freq[subdomain] = freq.get(subdomain, 0) + count

        return [str(count) + " " + domain for domain, count in freq.items()]
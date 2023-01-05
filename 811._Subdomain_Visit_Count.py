class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
​
        d = defaultdict(int)
        
        for i in cpdomains:
            times, domains = i.split(" ")
            domain_sep = domains.split(".")
            N = len(domain_sep)
            
            for j in range(N):
                n = ".".join(domain_sep[j:N])
                print(n)
                d[n] += int(times)
            # print(times, domains, N)
        
        # print("domains", d)
        res = []
        for key,values in d.items():
            res.append(f"{values} {key}")
        # print(res)
        return res
    
    
    
    
    
    
'''
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
[
"900 google.mail.com",
    "900 .mail.com"
    "900 .com"
​
 "50 yahoo.com",
    "50 .com"
    
 "1 intel.mail.com",
    "1 .mail.com"
    "1 .com"
    
 "5 wiki.org"

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # if len(barcodes) 
        # barcodes.sort()
        c = Counter(barcodes)
        N = len(barcodes)
        i = 0
        res = [0] * N
        # N = len(barcodes)
        for k, f in c.most_common():
            # print(k , f)
            for _ in range(f):
                if i >= N: i = 1
                res[i] = k
                i += 2
        return res
                
            

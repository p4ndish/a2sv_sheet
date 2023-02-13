class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        left,right = 0,0
        N = len(chars)
        while right < N:
            count = 0
            curr = chars[right]
            while right < N and chars[right] == curr :
                count += 1
                right += 1
            
            count = str(count)
            chars[left] = curr
            left += 1
            if count != '1':
                for ch in count:
                    chars[left] = ch
                    left += 1
        return left
            
            
            
        
        
        
        
        
        return 0
    
    
    
'''
n = 2

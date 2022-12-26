class Solution:
    def isPalindrome(self, x: int) -> bool:
​
        if not str(x)[0].isdigit():
            return False
        
        rev = ""
        for i in str(x)[::-1]:
            rev += i
        print(int(rev), x)
        return True if int(rev) == x else False

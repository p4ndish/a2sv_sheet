class Solution:
    def simplifyPath(self, path: str) -> str:
        # print(path.split("/"))
        path = path.split("/")
        stack = []
        
        for i in range(len(path)):
            if path[i] == '..':
                if stack :
                    stack.pop()
            elif path[i] == '' or path[i] == '.':
                continue
            else:

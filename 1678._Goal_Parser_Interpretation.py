class Solution:
    def interpret(self, command: str) -> str:
        # to help me to see the next coming chr for () 
        command += "#"
        
        res = ""
        bl = ")al"
        for i in range(len(command)-1):
            if command[i] in bl:
                continue
            if command[i] == "G":
                res += "G"
            elif command[i] == "(" and command[i+1] == ")":
                res += "o"
            else:
                if command[i] not in bl:
                    res += "al"
        # print(res)
        return res

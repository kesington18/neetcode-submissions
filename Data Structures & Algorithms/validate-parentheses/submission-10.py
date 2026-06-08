class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for char in s:
            if char == "{" or char == "[" or char == "(":
                res.append(char)
            elif res and char == "}" and res[-1] == "{":
                res.pop() 
            elif res and  char == ")" and res[-1] == "(":
                res.pop()
            elif res and char == "]" and res[-1] == "[":
                res.pop()
            else:
                return False
        
        if res:
            return False
        else: 
            return True
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res, ind = [], 0  #index = 0

        while ind < len(s):
            j = ind # index = 0 therefore j = 0

            while s[j] != "#": # str[0] != # and we know that str[0] == a str of int so the condition is not met yet
                j += 1 #increase j by 1

            integerLength = int(s[ind:j]) # it gets the integer from the string and convert it to an integer

            res.append(s[j + 1: j + 1 + integerLength]) # we there for push the strings starting from  j which is 1 then we add 1 to it which is 2, 
            # starts from index 2 to 1+1+integerlength(5) = 7
            # that is it will stop at index 6

            ind = j + 1 + integerLength # index increases by 7 for the first loop
        return res
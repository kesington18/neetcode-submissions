from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        if len(s) != len(t):
            return False
        
        if sCounter != tCounter:
            return False
        return True
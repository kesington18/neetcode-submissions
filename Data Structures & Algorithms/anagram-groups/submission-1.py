from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for var in strs:
            srt = sorted(var)
            joinStr = "".join(srt)
            if joinStr not in hashmap:
                hashmap[joinStr] = [var]
            else:
                hashmap[joinStr].append(var)
        return list(hashmap.values())
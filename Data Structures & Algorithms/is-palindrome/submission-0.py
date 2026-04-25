import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # res = joined
        l = 0
        r = len(cleaned) - 1

        print(cleaned)
        while l <= r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
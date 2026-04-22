class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = [n for n in nums if n >= 0]
        i = 1
        while i in numSet:
            i += 1
        return i
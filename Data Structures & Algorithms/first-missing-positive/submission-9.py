class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = list(set(nums))

        numSet = [n for n in numSet if n >= 0]
        i = 1
        while i in numSet:
            i += 1
        return i
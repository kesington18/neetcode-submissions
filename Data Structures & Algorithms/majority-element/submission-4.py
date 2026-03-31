from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxCount = 0
        keyCount  = 0

        print(counts)
        for key, value in counts.items():
            if value > maxCount:
                maxCount = value
                keyCount = key 
        return keyCount
                
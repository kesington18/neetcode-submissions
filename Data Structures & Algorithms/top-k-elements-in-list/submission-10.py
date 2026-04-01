from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        sorted_keys = sorted(numCounter, key=numCounter.get, reverse=True)
        return sorted_keys[:k]
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        div = len(nums) // 3
        numCounter = Counter(nums)
        res = []

        
        if len(nums) <= 2 :
            return nums
        elif max(numCounter.values()) == 1:
            return []
        else:
            for key, value in numCounter.items():
                if value > div:
                    res.append(key)
                # print(key, value)
            return res

        # print(div, numCounter)
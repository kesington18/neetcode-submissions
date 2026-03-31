class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums):
            res = target - val
            if res in hashmap:
                return [hashmap[res], i]
            hashmap[val] = i
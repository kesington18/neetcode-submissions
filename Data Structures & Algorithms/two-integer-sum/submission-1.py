class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        lt = []

        for i in range(len(nums)):
            final = target - nums[i]
            if final in hashmap:
                lt.append(hashmap[final])
                lt.append(i)
            hashmap[nums[i]] = i
        return lt
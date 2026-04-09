import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            new_list = nums.copy()
            new_list.remove(nums[i])
            result = math.prod(new_list)
            res.append(result)
            
        return res
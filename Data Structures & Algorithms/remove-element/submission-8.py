
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        nums[:] = [x for x in nums if x != val]

        return len(nums)
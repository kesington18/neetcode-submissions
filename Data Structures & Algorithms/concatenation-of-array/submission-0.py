class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = nums.copy()
        nums.extend(new_list)
        return nums
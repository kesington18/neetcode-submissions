class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums

        m = n // 2
        Left = nums[:m]
        Right = nums[m:]

        Left = self.sortArray(Left)
        Right = self.sortArray(Right)
        l, r = 0, 0
        Left_len = len(Left)
        Right_len = len(Right)

        sorted_nums = [0] * n
        i = 0

        while l < Left_len and r < Right_len:
            if Left[l] < Right[r]:
                sorted_nums[i] = Left[l]
                l += 1
            else:
                sorted_nums[i] = Right[r]
                r += 1
            i += 1

        while l < Left_len:
            sorted_nums[i] = Left[l]
            l += 1
            i += 1

        while r < Right_len:
            sorted_nums[i] = Right[r]
            r += 1
            i += 1

        return sorted_nums
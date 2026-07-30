class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxNum = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxNum = max(maxNum, area)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return maxNum

"""
Area = Width * Height = (j - i) * min(height[i], height[j])
Width: 7 - 1 = 6
Height: min(7, 6) = 6
Area: 6 * 6 = 36
"""
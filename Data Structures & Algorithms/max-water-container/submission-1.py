class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula to calculate water:
        # (left - right) * min(heights[left], heights[right])

        res = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            # calculate with the current left and right
            area = (right - left) * min(heights[left], heights[right])
            res = max(res, area)
            # move the one that is lower than the other
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1

        return res
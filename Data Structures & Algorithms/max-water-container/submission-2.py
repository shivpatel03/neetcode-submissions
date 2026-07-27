class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula to calculate water:
        # (right - left) * min(heights[left], heights[right])

        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            # calculate water in each iteration
            area = (right - left) * min(heights[left], heights[right])
            max_water = max(area, max_water)

            # when to move each pointer:
            # move the pointer that has the lower height
            # this is because it is the limiting factor in each case
            # if we keep the lower number the same, it will never be able to go past a certain amount
            if (heights[right] < heights[left]):
                right -= 1
            else: 
                left += 1

        return max_water
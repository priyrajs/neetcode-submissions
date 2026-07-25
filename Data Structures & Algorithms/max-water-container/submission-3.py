class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1

        maxWater = 0
        while r > l:
            h = min(heights[r],heights[l])
            w = r-l
            maxWater = max(h*w, maxWater)
            if heights[r] > heights[l] :
                l += 1
            else:
                r -= 1
        return maxWater 
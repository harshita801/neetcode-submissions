class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        water_stored=0
        maxi=0
        while left<right:
            water_stored=min(heights[left],heights[right])*(right-left)
            maxi=max(maxi,water_stored)

            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return maxi
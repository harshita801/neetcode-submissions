class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxi=0
        for i in range(n):
            water_stored=0
            for j in range(i+1,n):
                water_stored=min(heights[i],heights[j])* (j-i)
                maxi=max(maxi,water_stored)
        return maxi
        
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            leftMax = 0
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])

            rightMax = 0
            for j in range(i, n):
                rightMax = max(rightMax, height[j])
            water += min(leftMax, rightMax) - height[i]

        return water
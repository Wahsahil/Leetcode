class Solution:
    def trap(self, height):
        n = len(height)

        left = [0] * n
        left[0] = height[0]

        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        right = [0] * n
        right[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])

        trapped = 0

        for i in range(n):
            waterlevel = min(left[i], right[i])
            trapped += waterlevel - height[i]

        return trapped
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [0] * n
        right_height = [0] * n

        for i in range(1,n):
            left_height[i] = max(left_height[i-1],height[i-1])
            right_height[n-i-1] = max(right_height[n-i],height[n-i])

        water = 0
        for i in range(n):
            col_water = min(left_height[i], right_height[i]) - height[i]
            if col_water < 0:
                col_water = 0
            water += col_water
        
        return water
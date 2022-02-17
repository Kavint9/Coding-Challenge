# Leetcode problem: https://leetcode.com/problems/container-with-most-water/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        # dual pointers
        left = 0
        right = len(height ) -1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
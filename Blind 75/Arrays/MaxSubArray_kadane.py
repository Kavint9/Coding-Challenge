# Leetcode problem: https://leetcode.com/problems/maximum-subarray
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for val in nums[1:]:
            curr_sum = max(val, curr_sum + val)
            max_sum = max(max_sum, curr_sum)
        return max_sum
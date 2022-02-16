# Leetcode problem: https://leetcode.com/problems/maximum-product-subarray/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        output = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            # check prev max , prev min and current value in case prev both are negative
            temp = max(curr, max_so_far * curr, min_so_far * curr)
            # Similarly check for min so far
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp
            # global max,check with current max
            output = max(max_so_far, output)
        return output
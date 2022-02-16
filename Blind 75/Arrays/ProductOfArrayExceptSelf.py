# Leetcode problem: https://leetcode.com/problems/product-of-array-except-self/
# Time Complexity: O(N) - 2 loops one to calculate product of elements to the right
# Space Complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Store all the values to the right of each element
        product = [1 for _ in range(len(nums))]

        # construct array storing product of values to the right
        for i in range(len(nums) - 2, -1, -1):
            product[i] = product[i + 1] * nums[i + 1]

        # store the products to the left
        product_to_left = 1
        for i in range(len(nums) - 1):
            product[i] *= product_to_left
            product_to_left *= nums[i]

        product[-1] = product_to_left
        return product


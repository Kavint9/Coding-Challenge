# Leetcode problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time Complexity: O(LogN)
# Space Complexity: O(1)
# if middle is greater than the right element, then the min is to the right
# else mid is to the left

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        output = None

        def binarySearch(arr, left, right):
            mid = int(left + ((right - left) / 2))

            if mid == 0 and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]

            if mid == len(arr) - 1 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # Check if mid satisfies the minimum condition, if rotated n times then the min is the start
            if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                return arr[mid]

            # If not then check which direction to shift
            if arr[mid] > arr[right]:
                return binarySearch(arr, mid + 1, right)
            else:
                return binarySearch(arr, left, mid - 1)

        return binarySearch(nums, 0, len(nums) - 1)


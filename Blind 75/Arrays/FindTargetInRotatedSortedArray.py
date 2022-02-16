# Leetcode problem: https://leetcode.com/problems/search-in-rotated-sorted-array
# Time Complexity: O(LogN)
# Space Complexity: O(1)



# Binary Search
def bin_search(arr, left, right, target):
    if left > right:
        return -1

    mid = int(left + (right -left ) /2)

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return bin_search(arr, mid +1, right, target)
    else:
        return bin_search(arr, left, mid -1, target)


# Search for min
def minIndex(arr, left, right):
    mid = int(left + (right - left ) /2)

    if mid == 0:
        if arr[mid] > arr[mid +1]:
            return mid +1
        else:
            return mid

    if mid == len(arr) -1 and arr[mid] < arr[mid -1]:
        return mid

    if arr[mid] < arr[mid +1] and arr[mid] < arr[mid -1]:
        return mid

    if arr[mid] > arr[right]:
        return minIndex(arr, mid +1, right)
    else:
        return minIndex(arr, left, mid -1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge cases
        if not nums:
            return -1

        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        # Search for min value
        min_ind = minIndex(nums, 0, len(nums ) -1)

        if nums[min_ind] == target:
            return min_ind

        # Binary Search to the right or the left based on if target is less than or greater than min
        target_ind = bin_search(nums, min_ind, len(nums ) -1, target) \
            if target > nums[min_ind] and target <= nums[len(nums ) -1]  else \
            bin_search(nums, 0, min_ind, target)

        return target_ind














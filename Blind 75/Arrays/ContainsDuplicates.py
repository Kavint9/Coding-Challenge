# Leetcode problem: https://leetcode.com/problems/contains-duplicate
# Time Complexity: O(N)
# Space Complexity: O(N) - use hashset to reduce time complexity
# Alternate approach - sort array and check consecutive element O(NLogN)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        return False

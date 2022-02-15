# Leetcode problem: https://leetcode.com/problems/two-sum/
# Time Complexity: O(N)
# Space Complexity: O(N) - using a hashmap to reduce time complexity
# alternate approach
# sacrifice time for space - sort array and use two pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        output = list()
        for i in range(len(nums)):
            if target - nums[i] in hashmap.keys():
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i
        return []
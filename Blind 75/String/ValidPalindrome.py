# Leetcode problem: https://leetcode.com/problems/container-with-most-water/
# Time Complexity: O(N) - loop through the characters twice
# Space Complexity: O(N) - storing stripped string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ""
        for el in s:
            if el.isalnum():
                final += el.lower()

        left = 0
        right = len(final ) -1
        while left < right:
            if final[left] != final[right]:
                return False
            left += 1
            right -= 1
        return True
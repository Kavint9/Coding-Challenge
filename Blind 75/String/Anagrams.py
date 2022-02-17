# Leetcode problem: https://leetcode.com/problems/valid-anagram/
# Time Complexity: O(N)
# Space Complexity: O(1) 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        slist = list(s)
        scharlist = [0 for _ in range(27)]
        for char in slist:
            scharlist[ord(char) - ord('a')] += 1

        for element in t:
            if scharlist[ord(element) - ord('a')] == 0:
                return False
            else:
                scharlist[ord(element) - ord('a')] -= 1
        return True
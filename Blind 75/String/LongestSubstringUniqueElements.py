# Leetcode problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(N)
# Space Complexity: O(N) - hashset
# Alternate approach: use a hashmap to store the index of the previously encountered character move left to that index


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        length = 0
        hashset = set()
        slist = list(s)
        left = 0
        right = 0
        # Loop through the list
        while right < len(slist):
            # Check if current element is currently in the hashset
            if slist[right] in hashset:

                # update length only when duplicate is seen
                length = max(length, len(hashset))

                # move left pointer so that the values till the duplicate are removed
                while slist[left] != slist[right]:
                    hashset.remove(slist[left])
                    left += 1
                    # remove the duplicate
                hashset.remove(slist[left])
                left += 1

            # add new value
            hashset.add(slist[right])
            right += 1

        # check hashset at the end
        return max(length, len(hashset))
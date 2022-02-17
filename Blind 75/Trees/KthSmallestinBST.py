# Leetcode problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Time Complexity: O(N)
# Space Complexity: O(1) - hashset

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
value = 0
def DFS(node, count):
    global value
    if not node:
        return count

    count = DFS(node.left, count)

    count -= 1
    if count == 0:
        value = node.val

    count = DFS(node.right, count)

    return count


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global value
        # Perform DFS in-order traversal, take the kth visited item and return
        DFS(root, k)
        return value
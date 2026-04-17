# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal = True

        def isbalance(root):
            if not root: return 0

            leftTree = isbalance(root.left)
            rightTree = isbalance(root.right)

            if abs(leftTree - rightTree) > 1:
                self.isBal = False

            return max(leftTree, rightTree) + 1

        isbalance(root)

        return self.isBal
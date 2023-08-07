# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # can start at any node
        # same tree is considered a subtree

        # check if node is equal to subtree node
            # if it is
                # check for same tree
                # return true if same
                # continue otherwise
        # return false at the end if we never have same tree

        # is same tree function
            # recursively check if root and subroot have same value
            # return False if not same value
            # return True when subroot and root are both None

        if subRoot is None:
            return True
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        
    def isSameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
            
        if root is None or subRoot is None:
            return False
            
        if root.val != subRoot.val:
            return False
            
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
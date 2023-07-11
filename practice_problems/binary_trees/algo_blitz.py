'''
Q. Given an binary tree and a target subtree, determine if the original tree contains a target subtree. A subtree of a tree is a tree consisting of a node in the original tree and all of its descendants while maintaining the same structure.


Q. Given a binary tree, return the values of the nodes when facing the tree from the right side (from top to bottom).

'''
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def target_subtree(tree, subtree) -> bool:

    # we want to traverse the root tree until we find a node that matches subtree root

    # once that happens, we traverse them together until subtree is finished while comparing values

    # if any of the comparisons are false, return false

    # if there is never a matching node in the first place, return false

    if not tree:
        return False
    
    def compare_trees(tree, subtree):
        if not subtree:
            return True
            
        if subtree and not tree:
            return False

        if tree.value != subtree.value:
            return False
        
        return compare_trees(tree.left, subtree.left) and compare_trees(tree.right, subtree.right)
    
    if tree.value == subtree.value:
        return compare_trees(tree, subtree)
    
    target_subtree(tree.left, subtree)
    target_subtree(tree.right, subtree)


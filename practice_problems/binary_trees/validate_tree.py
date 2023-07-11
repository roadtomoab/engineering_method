'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, determine if it is a valid binary search tree (BST).

Examples:
• Given a binary tree:
        2
       / \
      1   3
// returns True

• Given a binary tree:
        1
       / \
      2   3
// returns False

🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right      


        
def validate_bst(root: TreeNode) -> bool:

    def helper(node, max, min):

        # for left side of the tree, root is the max

        # for right side of the tree, root is the min

        if node is None:
            return True
        
        # if it's ever greater than the max value, or less than the min value, we return false
        if node.value >= max or node.value <= min:
            return False
        
        return helper(node.left, node.value, min) and helper(node.right, max, node.value)
    
    return helper(root,float('inf'),float('-inf'))
    




# Test Cases
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14, TreeNode(13))))
tree4 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(9)), TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(validate_bst(None), True)
print(validate_bst(tree1), True)
print(validate_bst(tree2), False)
print(validate_bst(tree3), True)
print(validate_bst(tree4), False)
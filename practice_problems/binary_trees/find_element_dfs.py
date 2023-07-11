'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree and a target element's value, determine if the tree contains the target using depth first search (DFS).

Examples:
• Given a binary tree:
                 3
                / \
              29   4
              /     \
             2       2
                    /
                   9
• For target: 1 // returns False
• For target: 2 // returns True

🔎 EXPLORE
What are some other insightful & revealing test cases?
- if input tree is null, we can return false
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: recursive case
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

def find_dfs(root: TreeNode, target: int) -> bool:
    
    # base case - if we reach the end without finding the node, we return true
    if not root:
        return False
    
    if root.value == target:
        return True
    
    left_node = find_dfs(root.left, target)
    right_node = find_dfs(root.right, target)

    return left_node or right_node

# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_dfs(None, 1), False)
print(find_dfs(tree1, 9), True)
print(find_dfs(tree1, 1), False)
print(find_dfs(tree1, 2), True)
print(find_dfs(TreeNode(1), 2), False)
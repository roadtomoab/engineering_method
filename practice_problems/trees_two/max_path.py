'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a non-empty binary tree, find the maximum path sum.

Note:
• A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example:
• Given a binary tree: 
           1
          / \    
         2   3
        /     
      -1   
// returns 6 (1 + 2 + 3)

🔎 EXPLORE
What are some other insightful & revealing test cases?
- if only one node in tree, return value of that node
- null node would return None
- we essentially need to be checking if adding the next number helps or hurts us
    - for example, we know that between -1, -1+2, and 2, 2 is the greatest
- we also need to be checking for the same path

- i guess brute force would actually be checking the sum of every path and then taking the max
    - how would we do this?

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
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def mps(root: TreeNode) -> int:
    max_sum = float('-inf')

    def dfs(root):
        nonlocal max_sum

        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        max_sum = max(max_sum, root.value + left + right, 0)

        return max(root.value + left, root.value + right, 0)
    
    dfs(root)
    return max_sum

root = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(3)
left2 = TreeNode(3)

root.left = left1
root.right = right1
left1.left = left2

print(mps(root))

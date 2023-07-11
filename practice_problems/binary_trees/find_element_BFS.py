'''
Q. Given a binary tree and a target element's value, determine if the tree contains the target using breadth first search (BFS).

🔎 EXPLORE
What are some other insightful & revealing test cases?
- BFS is breadth first search - meaning that it looks across
 

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
from collections import deque

def find_bfs(root, target):

    if root is None:
        return False
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val == target:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False
    


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree1 = TreeNode(3, TreeNode(29, TreeNode(2)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_bfs(None, 1), False)
print(find_bfs(tree1, 9), True)
print(find_bfs(tree1, 1), False)
print(find_bfs(tree1, 2), True)
print(find_bfs(TreeNode(1), 2), False)
'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, print level order traversal so that nodes of all levels are printed in several lines

Examples:
• Given a binary tree:
                 1
                / \ 
               2   3
// returns [[1], [2, 3]]

• Given a binary tree:
                 1
                / \
               2   3
              / \
             4   5

// returns [[1], [2, 3], [4, 5]]

🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()

- return empty array if none
- we're gonna need to iterate the entire tree no matter what
- need to track levels
- we can have our output index correspond to the level
    - first level (root value) will always be index 0
    - second level index 1, etc
    - can have level be 0 indexed as well to make it easier
- can do dfs or bfs tbh, so let's do bothingtonski
 

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

def printByLevel(root: TreeNode) -> 'list[list[int]]':

    result = []

    def dfs(node, level=1):

        if node is None:
            return 

        if len(result) < level:
            result.append([node.value])
        if len(result) == level:
            result[level-1].append(node.value)
        
        if node.left:
            dfs(node.left, level + 1)
        if node.right:
            dfs(node.right, level + 1)
    
    dfs(root)

    return result

from collections import deque

def printByLevelBFS(root: TreeNode) -> 'list[list[int]]':

    if root is None:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

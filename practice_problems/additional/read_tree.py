'''
❓ PROMPT
In many but not all languages, humans read from top to bottom, left to right. This problem is convert a tree to a list of values in this reading order. Since computer scientists draw trees with the root at the top, the first node we read is that one, followed by the nodes at the first level down (only at most two nodes), then the third level, etc. For example:

      a
    /  \
   b     c
 /
d

We would read this as [a, b, c, d].

Write a function that generates a list of the values in a binary tree in this reading order.

Example(s)
treeToArray(new BTNode("a")) - returns ['a']
treeToArray(new BTNode("a", new BTNode("b"))) - only left child, returns ['a', 'b']
treeToArray(new BTNode("a", null, new BTNode("b"))) - only right child, returns ['a', 'b']
treeToArray(new BTNode("a", new BTNode("b"), new BTNode("c"))) - basic tree with both left and right children, , returns ['a', 'b', 'c']

 

🔎 EXPLORE
List your assumptions & discoveries:
- valid binary tree input, including none and one node
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- looks like a BFS
Time: O(n) - traverse all nodes
Space: O(n) - output array of size n, queue of size n
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function treeToArray(root)
function tree_to_array(root):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

from collections import deque

class BTNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def treeToArray(root: BTNode) -> 'list[int]':

    if root is None:
        return []

    result = []

    def bfs(root):

        nonlocal result

        queue = deque([root])

        while queue:
            node = queue.popleft()

            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    bfs(root)
    return result

print(treeToArray(None))
print(treeToArray(BTNode("a", BTNode("b", BTNode("c"), BTNode("d")))))
print(treeToArray(BTNode("a", BTNode("b", BTNode("c", BTNode("d"))))))

complete = BTNode('a',
  BTNode('b',
    BTNode('d'),
    BTNode('e')
  ),
  BTNode('c',
    BTNode('f'),
    BTNode('g')
  )
)
print(treeToArray(complete))


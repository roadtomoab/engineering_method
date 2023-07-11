'''
❓ PROMPT
Given a binary tree, modify each node value to be the sum of itself and its parent node. Return the root node of the modified tree.

Example(s)
       1
   2       4
should turn into
      1
  3       5

       1
   3       4
3   _    _   _
should turn into
       1
   4       5
6    _   _   _
 

🔎 EXPLORE
List your assumptions & discoveries:
- not changing the parent node, only changing children nodes
-
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: recursive approach
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- what would base case be? when node doesn't have any children
- recursive case would be when there are children - we'll change value of the children nodes by adding parent node (current) value to it
 

🛠️ IMPLEMENT
function immediateParentSum(root) {
def immediateParentSum(root: Node) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def immediateParentSum(root):

    # base case
    if not root.left and not root.right:
        return root
    
    # recursive case
    if root.left:
        root.left = immediateParentSum(root.left)
        root.left.val += root.val
    if root.right:
        root.right = immediateParentSum(root.right)
        root.right.val += root.val
    
    return root

root = Node(1)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_6 = Node(6)

# link the nodes to form the tree
#    1
#  1    2
# 3 4    6


root.left = node_1
root.right = node_2
node_1.left = node_3
node_1.right = node_4
node_2.right = node_6

print(immediateParentSum(root))
print(root.val == 1)
print(root.left.val == 2)
print(root.left.left.val == 4)
print(root.left.right.val == 5)
print(root.right.val == 3)
print(root.right.right.val == 8)
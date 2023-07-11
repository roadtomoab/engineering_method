'''
❓ PROMPT
Given a binary tree and a *target* value, remove the subtrees whose root equals that value. 

As a second step, modify this function to take a function as a parameter instead of a target value. The *predicate* function should take a tree node as a parameter and return true if that subtree should be pruned. You should test this with a multiple predicate functions to prune in different ways. You can start with a predicate function that matches the behavior in the initial problem.

Example(s)
        1 <--- root
    /       \
   2         3
 /   \     /   \
4     5   6     7

Removing the subtree rooted at 3 would result in the following:
     1
    /
   2
 /   \
4     5

prune(root, 3)
root.right == null

A method isEvenValueOver2(node) is passed into this conditional prune.
conditionalPrune(root, isEvenValueOver2)
root.left.left == null
root.right.left == null
 

🔎 EXPLORE
List your assumptions & discoveries:
- if tree passed in is null, return null
- only one of target value in tree
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- dfs style recursion to find target node
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- base case is when root is null - return null
- recursive case
- if value is the target, then we set left and right nodes to null
 

🛠️ IMPLEMENT
Prune subtrees with a root matching the *target*
function prune(root, target) {
def prune(root: Node, target: int) -> Node:

Prune subtrees with a root matching the criteria from a *predicate* boolean function.
function conditionalPrune(root, predicate) {
def conditionalPrune(root: Node, predicate) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right 

def prune(root, target):

    if root is None:
        return None
    
    if root.val == target:
        return None

    root.left = prune(root.left, target)
    root.right = prune(root.right, target)

    return root

print(prune(None, 5) == None)

tree = Node(1,
  Node(2,
    Node(4),
    Node(5),
  ),
  Node(3,
    Node(6),
    Node(7),
  ))

sameTree = Node(1,
  Node(2,
    Node(4),
    Node(5),
  ),
  Node(3,
    Node(6),
    Node(7),
  ))

def compareTrees(a, b):
  if not a and not b: return True
  elif not a or not b: return False
  else: return a.val == b.val and \
  compareTrees(a.left, b.left) and \
  compareTrees(a.right, b.right)

prune(tree, 100000)
print(compareTrees(tree, sameTree) == True)

prune(tree, 7)
print(tree.right.right == None)

prune(tree, 3)
print(tree.right == None)

print(prune(tree, 1) == None)

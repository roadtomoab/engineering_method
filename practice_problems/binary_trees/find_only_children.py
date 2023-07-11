'''
❓ PROMPT
Given a binary tree, find all nodes that have only one child. Return an array of node values representing each single-child parent in any order.

Example(s)
           1
       2       3
     _   4   _   _
    
should return [2]

           12
       3       4
    1    _   6   _
    
should return [3, 4]

           12
       3       4
    1    _   6   _
  9  _      _ _
    
should return [3, 1, 4]
 

🔎 EXPLORE
List your assumptions & discoveries:
- if there are no empty children, return an empty array
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
- return when root is none 
- if a node has only one child, add that child to the output array
 

🛠️ IMPLEMENT
function hasSingleChildren(root) {
def hasSingleChildren(root: Node) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def hasSingleChildren(root):

    results = []

    def helper(node):

        if not node:
            return
        
        if node.left and not node.right:
            results.append(node.value)
        elif node.right and not node.left:
            results.append(node.value)
        helper(node.left)
        helper(node.right)
        
    helper(root)    
    return results

print(hasSingleChildren(None) == [])

root = Node(1)
print(hasSingleChildren(root) == [])

#   1
# 2
root = Node(1,
  Node(2))
print(set(hasSingleChildren(root)) == set([1]))

#   1
# 2   3
root = Node(1,
  Node(2),
  Node(3))
print(hasSingleChildren(root) == [])

#     1
#  2     3
# _ 4   _ _
root = Node(1,
  Node(2,
    None,
    Node(4)),
  Node(3))
print(set(hasSingleChildren(root)) == set([2]))

#     12
#  3     4
# 1 _   6 _
root = Node(12,
  Node(3,
    Node(1)),
  Node(4,
    Node(6)))
print(set(hasSingleChildren(root)) == set([3,4]))

#     12
#   3     4
#  1 _   6  _
# 9 _   _ _
root.left.left.left = Node(9)
print(set(hasSingleChildren(root)) == set([3,1,4]))

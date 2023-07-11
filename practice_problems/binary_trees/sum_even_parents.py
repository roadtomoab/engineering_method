'''
❓ PROMPT
Given a binary tree, return the sum of all nodes with an even-valued parent node.

Example(s)
           6
       7       8
    2    7   1   3
result = 19 (7 + 8 + 1 + 3)

           2
       5       9
result = 14 (5 + 9)

           2
    null     null
result = 0
 

🔎 EXPLORE
List your assumptions & discoveries:
- if there are no even parents, we return 0
- has to be a parent node, so it must have at least one child
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: recursive
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- if null, return 0
- if node is even and has a child, add the value to our total result
 

🛠️ IMPLEMENT
function sumNodesWithEvenParent(root) {
def sumNodesWithEvenParent(root: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def sumNodesWithEvenParent(root):

    sum = 0

    def addEvens(node):
        nonlocal sum

        if not node:
            return
        
        if node.value % 2 == 0 and (node.left or node.right):
            if node.left:
                sum += node.left.value
            if node.right:
                sum += node.right.value
        
        addEvens(node.left)
        addEvens(node.right)
    
    addEvens(root)
    return sum



print(sumNodesWithEvenParent(None) == 0)

#     6
#  7     8
# 2 7   1 3
root = Node(6,
  Node(7,
     Node(2),
     Node(7)
  ),
  Node(8,
      Node(1),
      Node(3)
  )
)
print(sumNodesWithEvenParent(root) == 19)

#  2
# 5 9
root = Node(2,
  Node(5),
  Node(9))
print(sumNodesWithEvenParent(root) == 14)

# 2
root = Node(2)
print(sumNodesWithEvenParent(root) == 0)

# 1
root = Node(1)
print(sumNodesWithEvenParent(root) == 0)

#  1
# 5 9
root = Node(1,
  Node(5),
  Node(9))
print(sumNodesWithEvenParent(root) == 0)

#  1
# 2 2
root = Node(1,
  Node(2),
  Node(2))
print(sumNodesWithEvenParent(root) == 0)

#    1
#  2   2
# 9   4 1
root = Node(1,
  Node(2,
     Node(9)
  ),
  Node(2,
      Node(4),
      Node(1)
  )
)
print(sumNodesWithEvenParent(root) == 14)

#    1
#  1
# 1 1
root = Node(1,
  Node(1,
     Node(1),
     Node(1)
  )
)
print(sumNodesWithEvenParent(root) == 0)

#    6
#  8
# 4 2
root = Node(6,
  Node(8,
     Node(4),
     Node(2)
  )
)
print(sumNodesWithEvenParent(root) == 14)

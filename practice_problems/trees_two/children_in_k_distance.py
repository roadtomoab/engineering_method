'''
❓ PROMPT
Given a binary tree, a target node, and integer k, return an array of all children that are k distance away from the target node.

Example(s)
           1 <--- root
    2            3
 4     5      6     7
8 9  10 11  12 13 14 15

allChildrenKDistance(root, 2, 2) == {8,9,10,11}
allChildrenKDistance(root, 6, 1) == {12,13}
 

🔎 EXPLORE
List your assumptions & discoveries:
- if the target node is not present, return an empty array
- if there are no children k distance away, or no children of target node period, return an empty array
- input of None should also return an empty array
- k distance is measured by level essentially, so 1 distance we would just return it's children
- assuming that there's only one target
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) - iterating through our tree
Space: O(n) - output will be size of our tree in worst case

- we'll definitely iterate through the tree - DFS or BFS? I think BFS since we're finding the distance between nodes, and this way we won't go farther than needed
- we'll also need to keep track of a distance / level variable, that will start when we reach our target, and stop when we reach the given distance
- we'll be creating an array to store the children k distance away, potentially of size n, so
 

📆 PLAN
Outline of algorithm #: 

- if root is none we can return an empty array
- using BFS so we'll define a queue with the root in it
- we'll also define a result array
- while we have a queue:
    - have a level variable
    - pop out of the queue
    - if value of node is target:
        - we'll save that level
    - check if current level - k = saved level:
        - add value to output array
    - if current level > saved level + k:
        - return early
    - add left and right to queue
- return results
 

🛠️ IMPLEMENT
function allChildrenKDistance(root, target, k) {
def allChildrenKDistance(root: Node, target: int, k: int) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

- if root is none we can return an empty array
- using BFS so we'll define a queue with the root in it
- we'll also define a result array
- while we have a queue:
    - have a level variable
    - pop out of the queue
    - if value of node is target:
        - we'll save that level
    - check if current level - k = saved level:
        - add value to output array
    - if current level > saved level + k:
        - return early
    - add left and right to queue
- return results

'''
from collections import deque

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def allChildrenKDistance(root: Node, target: int, k: int) -> 'list[int]':
  def findChildren(node: Node, depth: int = 0, foundTarget=False) -> 'list[int]':
    if not node:
      return []

    if node.value == target:
      foundTarget = True
    if depth == k and foundTarget:
      return [node.value]

    if foundTarget:
      depth += 1

    return findChildren(node.left,  depth, foundTarget) + \
        findChildren(node.right, depth, foundTarget)

  return findChildren(root)


#   1
# 2   3


#           1
#     2           3
#  4    5      6     7
# 8 9 10 11  12 13 14 15
complete4levels = Node(1,
  Node(2,
    Node(4,
      Node(8),
      Node(9)),
    Node(5,
      Node(10),
      Node(11))),
  Node(3,
    Node(6,
      Node(12),
      Node(13)),
    Node(7,
      Node(14),
      Node(15))))


result = allChildrenKDistance(complete4levels, 5, 1)
print(set(result), {10,11})

result = allChildrenKDistance(complete4levels, 5, 2)
print(result == [] or result == None)

result = allChildrenKDistance(complete4levels, 2, 1)
print(set(result) == {4,5})

result = allChildrenKDistance(complete4levels, 2, 2)
print(set(result) == {8,9,10,11})

result = allChildrenKDistance(complete4levels, 6, 1)
print(set(result) == {12,13})

result = allChildrenKDistance(complete4levels, 6, 2)
print(result == [] or result == None)

result = allChildrenKDistance(complete4levels, 3, 1)
print(set(result) == {6,7})

result = allChildrenKDistance(complete4levels, 3, 2)
print(set(result) == {12,13,14,15})

result = allChildrenKDistance(complete4levels, 3, 3)
print(result == [] or result == None)

result = allChildrenKDistance(complete4levels, 10, 1)
print(result == [] or result == None)

# #           1 
# #     2           3
# #  4    5      6     7
# # 8   10    12    14
# root = Node(1,
#   Node(2,
#     Node(4,
#       Node(8)),
#     Node(5,
#       Node(10))),
#   Node(3,
#     Node(6,
#       Node(12)),
#     Node(7,
#       Node(14))))

# result = allChildrenKDistance(root, 1, 1)
# print(set(result) == {2,3})

# result = allChildrenKDistance(root, 1, 2)
# print(set(result) == {4,5,6,7})

# result = allChildrenKDistance(root, 1, 3)
# print(set(result) == {8,10,12,14})

# result = allChildrenKDistance(root, 5, 1)
# print(set(result) == {10})

# result = allChildrenKDistance(root, 5, 2)
# print(result == [] or result == None)

# result = allChildrenKDistance(root, 2, 1)
# print(set(result) == {4,5})

# result = allChildrenKDistance(root, 2, 2)
# print(set(result) == {8,10})

# result = allChildrenKDistance(root, 6, 1)
# print(set(result) == {12})

# result = allChildrenKDistance(root, 6, 2)
# print(result == [] or result == None)

# result = allChildrenKDistance(root, 3, 1)
# print(set(result) == {6,7})

# result = allChildrenKDistance(root, 3, 2)
# print(set(result) == {12,14})

# result = allChildrenKDistance(root, 3, 3)
# print(result == [] or result == None)

# result = allChildrenKDistance(root, 10, 1)
# print(result == [] or result == None)




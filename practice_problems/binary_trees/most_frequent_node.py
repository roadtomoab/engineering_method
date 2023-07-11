'''
❓ PROMPT
Given a binary tree with node values represented as integers, find and return the most frequent node value.

You can assume there will always be a most frequent node and no ties.

Example(s)
    5 <--- root
print(findMostFrequentNodeValue(root) == 5)

    5 <--- root
 10   5
print(findMostFrequentNodeValue(root) == 5)

    6 <--- root
  6   6
 6 6
print(findMostFrequentNodeValue(root) == 6)
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume that there is always a most requent node
- what should we return if root is empty?
 

Insightful & revealing test cases:
- all one value -> return that value
- two, two, and three -> return the one with three
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- recursively traverse a tree
- store occurences of each value in a dict
- iterate through dict and return value with highest occurence
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function findMostFrequentNodeValue(root) {
def findMostFrequentNodeValue(root: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findMostFrequentNodeValue(root):

    freq = {}

    def traverse(node):

        if node is None:
            return
        
        if node.value not in freq:
            freq[node.value] = 1
        else:
            freq[node.value] += 1

        if node.right:
            traverse(node.right)
        if node.left:
            traverse(node.left)
    
    traverse(root)

    max_val = float('-inf')
    answer = -1

    for node_value, n in freq.items():
        if n > max_val:
            max_val = n
            answer = node_value
    
    return answer


class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right 

root = Node(5)
print(findMostFrequentNodeValue(root) == 5)

#    5
# 10   5
root = Node(5,
  Node(10),
  Node(5))
print(findMostFrequentNodeValue(root) == 5)

#    6
#  6   6
# 6 6
root = Node(6,
  Node(6,
    Node(6),
    Node(6)),
  Node(6))
print(findMostFrequentNodeValue(root) == 6)

#     5
#  10   1
# 1  7
root = Node(5,
  Node(10,
    Node(1),
    Node(7)),
  Node(1))
print(findMostFrequentNodeValue(root) == 1)

#      5
#   2    1
# 3   7   10
#          10
root = Node(5,
  Node(2,
    Node(3),
    Node(7)),
  Node(1,
    None,
    Node(10,
      None,
      Node(10))))
print(findMostFrequentNodeValue(root) == 10)

#       1
#      2
#     3
#    4
#   5
#  6
# 3
root = Node(1,
  Node(2,
    Node(3,
      Node(4,
        Node(5,
          Node(6,
            Node(3)))))))
print(findMostFrequentNodeValue(root) == 3)
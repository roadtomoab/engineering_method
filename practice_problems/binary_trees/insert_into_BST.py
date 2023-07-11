'''

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary search tree and a target element's value, insert the target in the appropriate position.

Examples:
• Given a binary search tree:
              6
            /   \
           3     8
          / \ 
         2   4

• For target: 7 // returns:
              6
            /   \
           3     8
          / \    /
         2   4  7
        /     \
       1       5

• For target: 1 // returns:
              6
            /   \
           3     8
          / \
         2   4
        /
       1

🔎 EXPLORE
What are some other insightful & revealing test cases?
- if it's less - goes the left
- if it's greater - goes to the right
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- base case is when null - return 
- recursive case
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array

def insert_bst(root: TreeNode, target: int) -> TreeNode:
    # if it's empty, we'll return a node of just the target
    if not root:
        return TreeNode(target)
    curr = root
    while curr:
        # if target is less than value, move left
        if target < curr.value:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(target)
                return root
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(target)
                return root

def insert_bst_recursive(root, target):

    if not root:
        return TreeNode(target)
    
    if target < root.value:
        root.left = insert_bst_recursive(root.left, target)
    else:
        root.right = insert_bst_recursive(root.right, target)
    
    return root


# Test Cases
tree = TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
# print(arrayifyTree(insert_bst(tree, 7))) # [6, 3, 8, 2, 4, 7]
# print(arrayifyTree(insert_bst(tree, 5))) # [6, 3, 8, 2, 4, 7, 5]
# print(arrayifyTree(insert_bst(tree, 1))) # [6, 3, 8, 2, 4, 7, 1, 5]
# print(arrayifyTree(insert_bst(None, 1))) # [1]

print(arrayifyTree(insert_bst_recursive(tree, 7))) # [6, 3, 8, 2, 4, 7]
print(arrayifyTree(insert_bst_recursive(tree, 5))) # [6, 3, 8, 2, 4, 7, 5]
print(arrayifyTree(insert_bst_recursive(tree, 1))) # [6, 3, 8, 2, 4, 7, 1, 5]
print(arrayifyTree(insert_bst_recursive(None, 1))) # [1]

# Given tree:
#              6
#            /   \
#           3     8
#          / \    /
#         2   4  7
#        /     \
#       1       5
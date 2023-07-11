'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of integers sorted in ascending order, convert it to a height balanced BST.

Note:
• A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
• You must pick the smaller number when picking the "middle." In other words, when there are two numbers to choose from to pick the next child node, choose the smaller value (see example below).

Example:
• Given an array: [-10,-3,0,5,9]
// returns:
                0
               / \    
             -10   5 
               \    \
               -3    9

1. Choose 0 as a root node.
2. For left child node of 0, you have -10 and -3. According to the rule, you choose the smaller value -10.
3. Similar for choosing the right child node of 0, you are left with 5 and 9. Since 5 is smaller than 9, 5 becomes the right child node.

🔎 EXPLORE
What are some other insightful & revealing test cases?

- what about an array with even number of elemnts
- [1, 2, 3, 4, 5, 6]
        3
       / \
      1   4
       \  
        2

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
class TreeNode:
    def __init__(self, value, right=None, left=None) -> None:
        self.value = value
        self.right = right
        self.left = left

def sortedArrayToBST(nums: 'list[int]') -> TreeNode:

    def helper(start, count):

        if count == 0:
            return None

        mid = start + count // 2
        root = TreeNode(nums[mid])
        root.left = helper(start, mid - start)
        root.right = helper(mid+1, count - (mid - start + 1))
    
        return root
    
    return helper(0, len(nums))
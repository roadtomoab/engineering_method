'''
Q. Given a non-empty binary tree, find the maximum path sum.

A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Example:

Given a tree:
           1
          / \    
         2   3
        /     
      -1   
// returns 6 (1 + 2 + 3)


Q. Given an array of 0s, 1s, and 2s, sort them in-place in ascending order.

Examples:

Given an array: [2, 1] // returns [1, 2]
Given an array: [0, 2, 1, 0, 1, 2] // returns [0, 0, 1, 1, 2, 2]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

unsorted array of 0s, 1s, and 2s

[output] array.integer

sorted array of 0s, 1s, and 2s


Q. Given a positive hexadecimal integer represented as a string, convert it to a decimal form as an integer.

Examples:

Given: "D", returns 13`
Given: "84", returns "132"


Note: Your solution should have only one BST traversal and not use extra space beyond the recursive call stack.

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Given a binary search tree t, find the kth smallest element in it.

Note that kth smallest element means kth element in increasing order. See examples for better understanding.

Example

For

t = {
    "value": 3,
    "left": {
        "value": 1,
        "left": null,
        "right": null
    },
    "right": {
        "value": 5,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    }
}
and k = 4, the output should be
solution(t, k) = 5.

Here is what t looks like:

   3
 /   \
1     5
     / \
    4   6
The values of t are [1, 3, 4, 5, 6], and the 4th smallest is 5.

For

t = {
    "value": 1,
    "left": {
        "value": -1,
        "left": {
            "value": -2,
            "left": null,
            "right": null
        },
        "right": {
            "value": 0,
            "left": null,
            "right": null
        }
    },
    "right": null
}

and k = 1, the output should be
solution(t, k) = -2.

Here is what t looks like:

     1
    /
  -1
  / \
-2   0
The values of t are [-2, -1, 0, 1], and the 1st smallest is -2.

'''
'''
Recursion is certainly not the easiest approach to all of the following problems. 
However, it's useful to apply recursion on really easy problems to really understand the core pattern. 
Use recursion to write code for the following problems:

Sum all the elements in an array.

Remove all target elements from an array.

Return true if an array has palindrome values ([3, 2, 1, 2, 3] => true,  [3, 2, 1] => false)

Shift the elements in an array by 1 and move the last element to the first ([1, 2, 3, 4] => [4, 1, 2, 3])
'''

def sum_elements(arr):
    # go through each element and add it

    # base case will be when length is 1
    if len(arr) == 1:
        return arr[0]

    # recursive we'll add first element to function call with sliced array passed in
    return arr[0] + sumElements(arr[1:])

def remove_target(arr, k):
    # remove all elements that match k

    # base case will be when length is 0
    if len(arr) == 0:
        return arr
    
    # recursive case
    # if it's target element, we remove and pass the rest of the array
    if arr[0] == k:
        return removeTarget(arr[1:], k)
    else:
        return [arr[0]] + removeTarget(arr[1:], k)

# Return true if an array has palindrome values ([3, 2, 1, 2, 3] => true,  [3, 2, 1] => false)
def check_palindrome_helper(arr, start, end):
    # everything needs to return True to reach the end, so return True at the end
    # base case is when we reach the middle
    if start >= end:
        return True
    # if at any point start and end are different, return False
    if arr[start] != arr[end]:
        return False
    
    # recursive case
    return check_palindrome_helper(arr, start+1, end-1)

    # need to check each end
def check_palindrome(arr):
    return check_palindrome_helper(arr, 0, len(arr)-1)

def shift_and_move(arr):

    # base case is when list is empty
    if len(arr) == 0:
        return arr
    
    # recursive case


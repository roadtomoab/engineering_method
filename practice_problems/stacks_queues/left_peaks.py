'''
❓ PROMPT
Given an array of integers, return a sub-array of 'Left Peaks'. A Left Peak is defined as an element that is greater or equal
in value to all elements to its right.

Example(s)
find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]
find_left_peaks([3, 2, 1]) => [3, 2, 1]
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume that we have a valid input (array of n greater than or equal to 1)
- what should we return if no left peaks exist? an empty array?
 

Insightful & revealing test cases:
- [1,2,3] -> []
- [1, 1, 1] -> [1, 1]
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- iterate from the end of the array, comparing each element next to each other
- track a local max which stores max of all elements to the right of wherever we are in our iteration
- add numbers that meet the right condition
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function find_left_peaks(arr) {
def find_left_peaks(arr: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# this version essentially reverses the output

# def find_left_peaks(arr):

#     # result array
#     result = []

#     # local max
#     peak = float('-inf')

#     # loop from end of array
#     for i in range((len(arr)-1), 0, -1):
#         cur = arr[i]
#         prev = arr[i-1]

#         if cur > peak:
#             peak = cur
#         if prev >= peak:
#             result.append(prev)
    
#     return result

# print(find_left_peaks([1,4,3,1,2]))



# find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]

def find_left_peaks(arr):

    if not arr:
        return []

    stack = []
    # iterate through the array
    for i in range(len(arr)):
        # pop all elements smaller than the current element
        while stack and stack[-1] < arr[i]:
            stack.pop()
        
        stack.append(arr[i])
    
    return stack

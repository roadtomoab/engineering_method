'''
❓ PROMPT
Let's practice recursion by converting functions to and from recursive implementations. Copy the started code in the language of your choice below, then implement the missing functions and test! 

While reading the recursive implementation of *recursiveFactorial* as well as writing *recursiveMax*, consider the following:

1. What is my base case?
2. Which arguments do I need?
3. What do I do at each recursive step?

Example(s)
iterativeFactorial(3) -> 6
iterativeFactorial(4) -> 24

recursiveMax([4, 2, 7] -> 7
recursiveMax([1, -5, 0] -> 1
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

Python Starter Code

def recursiveFactorial(x: int) -> int:
  if x <= 1:
    return 1
  return x * recursiveFactorial(x - 1)

def iterativeFactorial(x: int) -> int:
  pass # TODO: implement

def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr: list[int], curMax=float('-inf'), i = 0) -> int:
  # curMax is an argument that defaults to null if not specified when calling recursiveMax()
  # i is an argument that defaults to 0 if not specified when calling recursiveMax()
  # return null if array is empty
  pass # TODO: implement
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def recursiveFactorial(x: int) -> int:
  if x <= 1:
    return 1
  return x * recursiveFactorial(x - 1)

def iterativeFactorial(x: int) -> int:
    factorial = 1

    while x > 1:
        factorial *= x
        x -= 1
    
    return factorial

def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr, curMax=float('-inf'), i = 0) -> int:
    if i >= len(arr):
        return curMax
    
    if arr[i] > curMax:
        curMax = arr[i]
    
    return recursiveMax(arr, curMax, i+1)



print(recursiveMax([4, 2, 7]))
print(recursiveMax([1, -5, 0]) == 1)
print(recursiveMax([1, 2, 7]) == 7)
print(recursiveMax([1, 0, -5]) == 1)
print(recursiveMax([-10, -3, -5]) == -3)
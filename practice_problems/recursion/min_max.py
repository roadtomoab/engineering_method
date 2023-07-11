'''
❓ PROMPT
Given an array, write 2 recursive functions to find the index of the minimum and maximum element in an array. 
If there's a tie-breaker, return the first occurrence.

Example(s)
findMinIndex([12, 1234, 45, 67, 1]) == 4
findMinIndex([10, 20, 30]) == 0
findMinIndex([8, 6, 7, 5, 3, 7]) == 4

findMaxIndex([12, 1234, 45, 67, 1]) == 1
findMaxIndex([10, 20, 30]) == 2
findMaxIndex([8, 6, 7, 5, 3, 7]) == 0
 

🔎 EXPLORE
List your assumptions & discoveries:
- return the INDEX
- assume that there's at least one element in the input array
 

Insightful & revealing test cases:
- [1] -> 0
- [3, 2, 1] -> 2
- [1, 1, 1] -> 0
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- recursive sauce
Time: O(n) - traversing entire array
Space: O(n) - stack size n
 

📆 PLAN
Outline of algorithm #: 
 - base case when length of array is 1
 - keep track of an index which is our answer
 - we'll compare i and i+1, keep the min, update our index in function call to keep track of it
 - 

🛠️ IMPLEMENT
function findMinIndex(array) {
function findMaxIndex(array) {
def findMinIndex(arr: list[int]) -> int:
def findMaxIndex(arr: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findMinIndex(array) -> int:

  def getMin(startIndex) -> int:
    if startIndex == len(array) - 1:
      return startIndex

    smallestIndex = getMin(startIndex + 1)

    if array[startIndex] > array[smallestIndex]:
      return smallestIndex
    if array[startIndex] < array[smallestIndex]:
      return startIndex
    else: # tie-breaker, get first occurrence
      return min(startIndex, smallestIndex)

  return getMin(0)

print(findMinIndex([1,2,3,0]))




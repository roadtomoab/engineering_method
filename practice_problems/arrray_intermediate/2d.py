'''
❓ PROMPT
In this task, we're going to apply basic 2-dimensional matrix traversals to solve some simple problems. While working on these, look out for other patterns you may have seen previously. Each of these takes the row- and column-major traversals and composites them with simpler ideas you have almost certainly encountered in one-dimensional problems.

This task is two similar problems in one:
- First, write a function that returns the average of the smallest values in each _column_.
- Write a new version of this function that returns the average of the smallest value in each _row_.

Remember that since we represent a matrix as nested arrays (an array of arrays), many problems on a matrix can be broken down into two array patterns. This makes them easier to reason about and code. 

Example(s)
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
averageRowMinimum(matrix) == 4 (because average(5, 3) = 4)
 

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
 

🛠️ IMPLEMENT
function averageColumnMinimum(matrix) {
function averageRowMinimum(matrix) {

def averageColumnMinimum(matrix: list[list[int]]) -> float:
def averageRowMinimum(matrix: list[list[int]]) -> float:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def averageColumnMinimum(matrix) -> float:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    # numbers in the same column will have the same index in the different array elements
    # for each column
    total = 0

    for i in range(len(matrix[0])):

        minimum = float('inf')
        # in order to move down the column
        for j in range(len(matrix)):
            minimum = min(minimum, matrix[j][i])
        
        total += minimum
    
    result = total / len(matrix[0])
    
    return result

def averageRowMinimum(matrix) -> float:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    # numbers the same row will be ones in the same array element
    length = 0
    min_total = 0

    for row in matrix:
        minimum = float('inf')
        for num in row:
            if num < minimum:
                minimum = num
        min_total += minimum
        length += 1
    
    result = min_total / length

    return result


'''
PROMPT
Given two arrays of equal length, return an array summing them together with the second array being traversed in reverse.

Example(s)
array1 = [1, 2, 3]
array2 = [4, 6, 10]
result = [11, 8, 7]

Explanation: *array1* is being traversed from left to right and *array2* is traversed right to left, so 1+10 = 11, 2+6 = 8, and 3+4 = 7.

array1 = [1, 5, 10, 12]
array2 = [2, 4, 3, 5]
result = [6, 8, 14, 14]

Explanation: 1+5 = 6, 5+3 = 8, 10+4 = 14, and 12+2 = 14.
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume that arrays are always of equal length
- array will only contain ints
 

Insightful & revealing test cases:
- [] and [] --> []
- [1] and [1] --> 2
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- reverse the second array
- iterate over original first and reversed second, adding them together

Time: O(n + logn) - original sorting, plus iteration
Space: O(1) - can overwrite one of the arrays and return.  would be O(n) space if we want to return a completely new array

Algorithm 2:
- iterate from the beginning of the first while iterating from the end of the second
- add together
- return new array

Time: O(n)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 

- establish a left and right pointer, left at 0 and right at index len-1
- while left < len and right >= 0
    - add first[left] and second[right], overwrite first array

- return first array
 

🛠️ IMPLEMENT
function sumInReverse(arr1, arr2) {
def sumInReverse(arr1: list[int], arr2: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def sumInReverse(arr1: 'list[int]', arr2: 'list[int]') -> 'list[int]':

    left = 0
    right = len(arr1) - 1

    while left < len(arr1) and right >= 0:
        arr1[left] = arr1[left] + arr2[right]
        left += 1
        right -= 1
    
    return arr1

print(sumInReverse([1,2,3], [4,6,10])) # [11, 8, 7]
print(sumInReverse([1,5,10,12], [2,4,3,5])) # [6, 8, 14, 14]
print(sumInReverse([], [])) # []
print(sumInReverse([1], [1])) # [2]
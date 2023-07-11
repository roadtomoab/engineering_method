'''
❓ PROMPT
Given an array, reverse every sub-array formed by consecutive k elements.

Example(s)
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3
Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 5
Output: [5, 4, 3, 2, 1, 8, 7, 6]

Input: arr = [1, 2, 3, 4, 5, 6], k = 1
Output: [1, 2, 3, 4, 5, 6]

Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 10
Output: [8, 7, 6, 5, 4, 3, 2, 1] 
 

🔎 EXPLORE
List your assumptions & discoveries:
- assuming that the array is always elements already in perfect ascending order
- empty array returns empty array
- if k is >= length of the array, reverse the entire array
 

Insightful & revealing test cases:
- [], any k -> []
- [1,2,3], 3 -> [3,2,1]
- [1,2,3,4,5], 3 -> [3,2,1,4,5]
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: split into partitions of k and remaining array until we can't. reverse partitions of k and write to a new array
Time: O()
Space: O()

- honestly not sure with all of the splitting

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function reverse(arr, k) {
def reverse(arr: list[int], k: int) -> None:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def reverse(arr, k):
    if arr is None:
        return None

    # result = []

    # def reverse_sub_arr(sub_arr):
    #     if len(sub_arr) == k:
    #         sub_arr = sub_arr[::-1]
    #     for i in range(len(sub_arr)):
    #         result.append(sub_arr[i])
    
    for i in range(0, len(arr), k):
        sub_arr = arr[i:i+k]
        if len(sub_arr) <= k:
            sub_arr = sub_arr[::-1]
        new = i
        for j in range(len(sub_arr)):
            arr[new] = sub_arr[j]
            new += 1
        # reverse_sub_arr(sub_arr)
    
    return arr


    
arr = [1,2,3,4,5,6,7,8,9]
print(reverse(arr, 3))
print(arr == [3,2,1,6,5,4,9,8,7])

arr = [1,2,3,4,5,6,7,8,9]
print(reverse(arr, 4))
print(arr == [4,3,2,1,8,7,6,5,9])

arr = [1,2,3,4,5,6,7,8]
print(reverse(arr, 4))
print(arr == [4,3,2,1,8,7,6,5])

arr = [1,2,3,4,5,6,7,8]
print(reverse(arr, 5))
print(arr == [5,4,3,2,1,8,7,6])

arr = [1,2,3,4,5,6,7,8]
reverse(arr, 10)
print(arr == [8,7,6,5,4,3,2,1])

arr = [1,2,3,4,5,6]
reverse(arr, 1)
print(arr == [1,2,3,4,5,6])

arr = [1,2,3,4,5,6]
reverse(arr, 4)
print(arr == [4,3,2,1,6,5])

arr = [1]
reverse(arr, 1)
print(arr == [1])
reverse(arr, 2)
print(arr == [1])

arr = []
reverse(arr, 1)
print(arr == [])

print(reverse(None, 1) == None)
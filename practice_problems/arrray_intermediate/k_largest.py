'''
❓ PROMPT
Given an array of integers and an integer K, find the Kth largest value in the array. You can assume that K is always smaller than the length of the array.

Example(s)
findKthLargest([3,2,1,5,6,4], 2) == 5
findKthLargest([1,1,5,3,2,9], 4) == 2
 

🔎 EXPLORE
List your assumptions & discoveries:
- k will never exceed the length of the array
- is k also greater than 0?
- k of 1 means return the largest
 

Insightful & revealing test cases:
[1,2,3,4,5], 1 -> 5
[1], 1 -> k
[], 0 -> ?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- sort the array
- iterate k times from end of the array to get our result
Time: O(nlogn) - sorting is nlogn + n iteration
Space: O(1) - no extra space needed

Algorithm 2:
using a min heapski ingtons lolzingtonskiiii
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function findKthLargest(nums, k) {
def findKthLargest(nums: list[int], k: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

from heapq import heapify, heappushpop

def findKthLargest(nums, k):
    # holds k elements in heap
    heap = nums[:k]
    # make valid min heap
    heapify(heap)

    # iterate through rest of nums
    for num in nums[k:]:
        heappushpop(heap, num)
    return heap[0]
 

print(findKthLargest([10], 1) == 10)
print(findKthLargest([15,15,15], 2) == 15)

print(findKthLargest([3,2,1,5,6,4], 2) == 5)
print(findKthLargest([1,1,5,3,2,9], 4) == 2)

print(findKthLargest([10,20,30,40], 3) == 20)
print(findKthLargest([10,20,30,40], 2) == 30)
print(findKthLargest([10,20,30,40], 1) == 40)

print(findKthLargest([40,30,20,10], 3) == 20)
print(findKthLargest([40,30,20,10], 2) == 30)
print(findKthLargest([40,30,20,10], 1) == 40)

print(findKthLargest([4,2,3,4,1,6], 1) == 6)
print(findKthLargest([4,2,3,4,1,6], 2) == 4)
print(findKthLargest([4,2,3,4,1,6], 3) == 4)
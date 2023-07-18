'''
❓ PROMPT
Given an array containing numbers, convert this to a singly linked list and return the head of the list.

Example(s)
arrayToLL([1,2]) == "1 -> 2"
arrayToLL([1,2,3]) == "1 -> 2 -> 3"
 

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
function arrayToLL(array) {
def arrayToLL(array: list[int]) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def arrayToLL(nums: 'list[int]') -> ListNode:
    if len(nums) == 0:
        return None
    
    sentinel = ListNode(0)
    cur = sentinel

    for i in range(len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    
    return sentinel.next

def toString(head: ListNode) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

print(toString(arrayToLL([])) == "<empty>")
print(toString(arrayToLL([1])) == "1")
print(toString(arrayToLL([1,2])) == "1 -> 2")
print(toString(arrayToLL([1,2,3])) == "1 -> 2 -> 3")
print(toString(arrayToLL([5,0,3])) == "5 -> 0 -> 3")
print(toString(arrayToLL([8,7,8,8])) == "8 -> 7 -> 8 -> 8")
print(toString(arrayToLL([8,7,8,8,7])) == "8 -> 7 -> 8 -> 8 -> 7")
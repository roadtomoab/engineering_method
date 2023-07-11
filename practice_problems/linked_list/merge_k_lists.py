'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given K sorted linked lists, merge all the lists into one sorted list. Each linked list is sorted in ascending order.

Examples:
• Given a linked list: [] // returns []
• Given an array of linked lists (only the head pointers): 
    [[1, 4, 5], [1, 3, 4], [2, 6]] // returns: [1, 1, 2, 3, 4, 4, 5, 6]

🔎 EXPLORE
What are some other insightful & revealing test cases?
- all none => none
- [] [] [1] => [1]
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()

- using a min heap is a good solution
- we'll
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

# using a min heap

import heapq

def mergeKListsDivCon(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left, right = mergeKListsDivCon(lists[:mid]), mergeKListsDivCon(lists[mid:]) 
    return merge(left, right)
    
def merge(left, right):

    if left is None:
        return right
    if right is None:
        return left
    
    dummy = Node(0)
    curr = dummy
    
    while left and right:
        if left.val <= right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    
    if left:
        curr.next = left
    if right:
        curr.next = right
    
    return dummy.next


def mergeKLists(lists):

    current_head_values = []

    while any(lists):
        for i, LL in enumerate(lists):
            if LL:
                heapq.heappush(current_head_values, LL.val)
                lists[i] = lists[i].next
    dummy = Node(0)
    curr = dummy

    for _ in range(len(current_head_values)):
        curr.next = Node(heapq.heappop(current_head_values))
        curr = curr.next
    
    return dummy.next


LL1 = Node(1, Node(1, Node(3, Node(4))))
LL2 = Node(2, Node(2, Node(4, Node(5))))
LL3 = Node(8)

result = mergeKListsDivCon([LL1, LL2, LL3])

curr = result
while curr:
    print(curr.val)
    curr = curr.next





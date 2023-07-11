'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a sorted linked list, insert an element in the appropriate position.

Examples:
• Given a linked list: 1 ➞ 3 ➞ 4, target: 2 // returns 1 ➞ 2 ➞ 3 ➞ 4
• Given an empty linked list, target: 1  // returns 1

🔎 EXPLORE
What are some other insightful & revealing test cases?
None, 1 => 1
2 -> 3 -> 3 , 1 => 1 -> 2 -> 3
1 -> 2 -> 3 , 2 => 1 -> 2 -> 2 -> 3

 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- iterate through the list
- if element is greater than or equal to current element, insert it

Time: O(n) - iterate over n elements in the list
Space: O(n) - we'll use a copy to iterate and still return the correct head
 

📆 PLAN
Outline of algorithm #:
- deal with edge cases (input is none, or target is less than head value)
- track with dummy
- iterate while checking value of next
- if value of next is >= target, we'll insert:
    - temp = curr.next
    - curr.next = target
    - target.next = temp
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head):
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

#     - deal with edge cases (input is none, or target is less than head value)
#      - track with dummy
#      - iterate while checking value of next
#       - if value of next is >= target, we'll insert:
#     - temp = curr.next
#     - curr.next = target
#     - target.next = temp

def insert(head: ListNode, target: int) -> ListNode:
    if head is None:
        return ListNode(target)
    
    new_node = ListNode(target)

    if target <= head.value:
        new_node.next = head
        return new_node
    
    cur = head
    
    while cur and cur.next:
        if cur.next.value >= target:
            temp = cur.next
            new_node.next = temp
            cur.next = new_node
            return head
        cur = cur.next
    
    if cur and target >= cur.value:
        cur.next = new_node
    
    return head

            
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
# print(arrayify(insert(LL1, 2))) # [1, 2, 3, 4]
# print(arrayify(insert(LL2, -4))) # [-4, -3, -2, -1]
print(arrayify(insert(LL2, 0))) # [-3, -2, -1, 0]
# print(arrayify(insert(None, 1))) # [1]
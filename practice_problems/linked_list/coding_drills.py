'''
function swapValuePairs(head) - swap the data in each node without swapping pointers

function additionNext(head) - add to the value in each node by the value in the next node. The tail node has no next node so double its value

function firstRemoveEveryOther(head) - remove every other node starting with removing the head.

function rotateValuesRight(head) - move the values right without altering next pointers. The tail's value should become the head's new value.

function removeLastQuarterNodes(head) - remove the last 1/4 of the nodes in the linked list. How can this be solved without a length variable?

'''

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# function swapValuePairs(head) - swap the data in each node without swapping pointers

def swap_value_pairs(head):

    curr = head

    while curr and curr.next:
        curr.val, curr.next.val = curr.next.val, curr.val
    
        curr = curr.next.next

    return head
# function additionNext(head) - add to the value in each node by the value in the next node. The tail node has no next node so double its value

def addition_next(head):

    curr = head

    while curr and curr.next:
        curr.val += curr.next.val
        curr = curr.next
    
    if curr:
        curr.val *= 2
    
    return head

# function firstRemoveEveryOther(head) - remove every other node starting with removing the head.

def first_remove_every_other(head):
    if not head:
        return None
    
    head = head.next
    curr = head

    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
    
    return head

# function rotateValuesRight(head) - move the values right without altering next pointers. The tail's value should become the head's new value.

def rotate_values_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head

    # Find the length of the linked list
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next

    # Determine the number of rotations required
    rotations = k % length
    if rotations == 0:
        return head

    # Traverse the linked list to find the node at position length - rotations
    slow = fast = head
    for i in range(rotations):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    # Rotate the linked list
    new_head = slow.next
    slow.next = None
    fast.next = head

    return new_head

# 1 2 3 4 5
# 1 1
# 5 1 2 3 4

# function removeLastQuarterNodes(head) - remove the last 1/4 of the nodes in the linked list. How can this be solved without a length variable?a

def remove_last_quarter_nodes(head):
    pass

LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
LL2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))

new_list = remove_last_quarter_nodes(LL2)

while new_list:
    print(new_list.val)
    new_list = new_list.next


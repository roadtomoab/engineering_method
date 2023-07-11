'''
❓ PROMPT
We've been given a list of employees at the company, each person's seniority is denoted by a number, eg: Junior => 3, Senior => 5, and so on.

For each person on the list, we want to find an adjacent employee that outranks them in the list to become their mentor. Return a new list of the same length corresponding to the level of the mentor.

If someone can't find an adjacent superior, they should not be assigned a mentor so it should return their own level.

Example(s)
head = 3 -> 1 -> 3
assignMentors(head) == [3,3,3]

head = 5 -> 6 -> 9
assignMentors(head) == [6,9,9]

head = 2 -> 2 -> 2
assignMentors(head) == [2,2,2]

head = 2 -> 7 -> 4 -> 3 -> 5
assignMentors(head) == [7,7,7,5,5]
 

🔎 EXPLORE
List your assumptions & discoveries:
- outranking employee needs to be adjacent
- if no acceptable mentors, we'll be returning the original list
- do we choose the greater or lesser one??? seems important
- also, what if the only option for a mentor is someone who also needs a mentor?
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()

- will need a new list, otherwise changed values will impact what we're doing
- need to track prev, current, and next. 
- curr = head
- prev = None, prev.next = curr
- new_head = head

- iterate over list using while curr and curr.next
- if prev > curr, change cur value in new list
- if next > curr, change cur value
- increment
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function assignMentors(head) {
def assignMentors(head: Node) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

def assignMentors(head: Node) -> 'list[int]':

    results = []

    curr = head
    prev = Node(float('-inf'))
    prev.next = curr

    while curr and curr.next:
        # take maximum of prev, curr and next
        new_value = max(prev.value, curr.value, curr.next.value)
        results.append(new_value)
        prev = prev.next
        curr = curr.next
    
    if curr:
        results.append(max(prev.value, curr.value))
    
    return results

print(assignMentors(None) == None or assignMentors(None) == [])

head = Node(1) # 1
print(assignMentors(head) == [1])

head = Node(3, Node(1, Node(3))) # 3 -> 1 -> 3
print(assignMentors(head) == [3,3,3])

head = Node(5, Node(6, Node(9))) # 5 -> 6 -> 9
print(assignMentors(head) == [6,9,9])

head = Node(2, Node(2, Node(2))) # 2 -> 2 -> 2
print(assignMentors(head) == [2,2,2])

# 2 -> 7 -> 4 -> 3 -> 5
head = Node(2, Node(7, Node(4, Node(3, Node(5)))))
print(assignMentors(head) == [7,7,7,5,5])

# 8 -> 7 -> 5 -> 4 -> 3
head = Node(8, Node(7, Node(5, Node(4, Node(3)))))
print(assignMentors(head) == [8,8,7,5,4])

# 5 -> 6 -> 7 -> 8 -> 9
head = Node(5, Node(6, Node(7, Node(8, Node(9)))))
print(assignMentors(head) == [6,7,8,9,9])

head = Node(9, Node(6, Node(5))) # 9 -> 6 -> 5
print(assignMentors(head) == [9,9,6])
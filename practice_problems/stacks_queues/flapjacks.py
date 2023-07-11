'''
❓ PROMPT
A restaurant has a dedicated cook making flapjacks (pancakes) in the mornings. First, they're removed from the griddle and 
added to a stack as they're ready. Then, servers remove them from the stack to serve customers. 
The manager wants to serve fresh flapjacks, meaning they never want the stack to be taller than 4. 
At the same time, they want the stack never to be empty so that no orders have to wait for pancakes.

Write a function that takes a series of numbers representing flapjacks being added and removed from the stack 
(positive for fresh off the grill, negative for an order being served). 
Return a tuple (or pair), where the first value is true or false to reflect if the manager's constraints are always satisfied,
and the second value is the max height of the stack.

Example(s)
goldilockFlapjacks([2, -1]) => [true, 2]
goldilockFlapjacks([-1, 2]) => [false, 1]
goldilockFlapjacks([2, -1, 3, -3, 2, -1]) => [true, 4]
 

🔎 EXPLORE
List your assumptions & discoveries:
- return whether it follows the rules or not, and max height of the pancake stack
- can we assume that the stack will never be less than zero? return false if this is the case
- always at least one order
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- store pancakes in a stack
- track max
- if number of pancakes is ever less than zero, false
- if it ever breaks rules, false
- at end of iteration, return our boolen value and our max
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- initialize empty stack
- initialize a max value
- initialize a boolean value to true
- iterate through our array of values
- add / remove number of pancakes from each element to / from stack
 

🛠️ IMPLEMENT
function goldilockFlapjacks(pancakes) {
def goldilockFlapjacks(pancakes: list[int]) -> list:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def goldilockFlapjacks(pancakes):

    stack = []
    maxHeight = 0
    valid = True

    for i in range(len(pancakes)):
        if pancakes[i] >= 0:
            for n in range(pancakes[i]):
                stack.append("pancake")
            if len(stack) > maxHeight:
                maxHeight = len(stack)
                print()
                if maxHeight > 4:
                    valid = False
        else:
            num = pancakes[i] * -1
            for n in range(num):
                if stack:
                    stack.pop()
                if not stack:
                    valid = False
            
    return [valid, maxHeight]



print(goldilockFlapjacks([2]) == [True, 2])
print(goldilockFlapjacks([-2]) == [False, 0])
print(goldilockFlapjacks([4]) == [True, 4])
print(goldilockFlapjacks([5]) == [False, 5])
print(goldilockFlapjacks([4, -2, 1, -2]) == [True, 4])
print(goldilockFlapjacks([2, -1, 1, -1, 1]) == [True, 2])
print(goldilockFlapjacks([4, -2, 1, -2, 4]) == [False, 5])
print(goldilockFlapjacks([4, -2, 1, -2, -4]) == [False, 4])

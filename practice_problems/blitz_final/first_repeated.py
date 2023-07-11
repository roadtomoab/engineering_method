'''
❓ PROMPT
Given an array, return the first element is repeated if you were to traverse the array from left to right.

Example(s)
firstRepeatedElement([1, 2, 3, 2, 1, 1]) == 2
 

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
function firstRepeatedElement(arr) {
def firstRepeatedElement(arr: list[int]) -> int: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def firstRepeatedElement(arr):

    freq = {}

    for el in arr:
        if el in freq:
            return el
        else:
            freq[el] = 1
    
    return None

print(firstRepeatedElement([]) == None)
print(firstRepeatedElement([5]) == None)
print(firstRepeatedElement([5,5]) == 5)
print(firstRepeatedElement([5,10]) == None)
print(firstRepeatedElement([1, 2, 3, 4]) == None)
print(firstRepeatedElement([1, 2, 1, 3]) == 1)
print(firstRepeatedElement([7, 7, 1, 1]) == 7)
print(firstRepeatedElement([2, 8, 8, 8]) == 8)
print(firstRepeatedElement([1, 2, 3, 2, 1, 1]) == 2)
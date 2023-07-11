'''
❓ PROMPT
Given a non-negative int n, compute recursively (no loops) the number of occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4 (because 2+1+0+1).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while dividing (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example(s)
count8(8) == 1
count8(818) == 2
count8(8818) == 4  (because 2+1+0+1)
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume valid input of non negative integer
 

Insightful & revealing test cases:
- each 8 counts as one occurence, unless there's another 8 immediately to it's left, then it counts double
- 8 -> 1
- 88 -> 3

let's walk through 8818

- mod 10 to get rightmost digit
- check if it's 8
- if it is, we'll increment count
- pass in increased count and num / 10 to remove rightmost digit
- we'll need to track whether the last number checked was an eight, we can use a boolean flag
    - set initially to false
    - if we have an eight, set true
    - otherwise set false again
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) - need to iterate over entire input integer
Space: O(n) - recursive stack of size n
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function count8(n) {
def count8(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def count8(n: int) -> int:

    count = 0

    def helper(num, previousEight):
        nonlocal count

        if num == 0:
            return
        
        if num % 10 == 8:
            if previousEight:
                count += 2
            else:
                count += 1
            return helper(num // 10, True)
        return helper(num // 10, False)
    
    helper(n, False)
    return count

print(count8(8), 1)
print(count8(88), 3)
print(count8(8818), 4)


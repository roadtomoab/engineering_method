'''
❓ PROMPT
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while integer division by 10 removes 
the rightmost digit (126 / 10 is 12). Be aware that some languages require some special handling to do integer division while others do not.

*Python integer division*: x // y
*Javascript integer division*: Math.floor(x / y)

Example(s)
count7(7) == 1
count7(123) == 0
count7(717) == 2
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume that n is positive
- if input is none, return 0 still
 

Insightful & revealing test cases:
- 7 -> 1
- 727 -> 2
- None -> 0
- 1234 -> 0
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- recursive 
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #:
- turn into an array
- use helper function
- base case is when len of array is 0
- if we encounter a 7, add 1 in our return that calls the rest of the elements
- if not, call the rest of the elements
 

🛠️ IMPLEMENT
function count7(n) {
def count7(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# def count7(n):

#     digits = [int(digit) for digit in str(n)]

#     def helper(digits):
#         if len(digits) == 0:
#             return 0
        
#         if digits[0] == 7:
#             return 1 + helper(digits[1:])
#         else:
#             return helper(digits[1:])
    
#     return helper(digits)

def count7(n):
    if n == 0:
        return 0
    
    if n % 10 == 7:
        return 1 + count7(n // 10)
    
    return count7(n // 10)


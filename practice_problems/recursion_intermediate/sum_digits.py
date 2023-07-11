'''
❓ PROMPT
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example(s)
sumDigits(12) == 3
sumDigits(49) == 13
sumDigits(126) == 9
 

🔎 EXPLORE
List your assumptions & discoveries:
- return the sum of digits
 

Insightful & revealing test cases:
- one digit number, return just that number
- 1 -> 1

- one digit would be our base case - just return that number
- add rightmost digit + sumDigits(without right digit)
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) - iterating over the entire number
Space: O(n) - call stack of size n
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function sumDigits(n) {
def sumDigits(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def sumDigits(n: int) -> int:

    if n < 10:
        return n

    return (n % 10) + sumDigits(n // 10)

print(sumDigits(12) == 3)
print(sumDigits(49) == 13)
print(sumDigits(126) == 9)
print(sumDigits(3) == 3)
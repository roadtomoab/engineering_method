'''
❓ PROMPT
Euclid's algorithm for finding the greatest common divisor (GCD) of two numbers *a* and *b* is:

euclidGCD(a, 0) := a
euclidGCD(a, b) := gcd(b, a mod b) 

Write a function that implements Euclid's algorithm and finds the GCD of two numbers. 

Check out this video https://www.youtube.com/watch?v=Jwf6ncRmhPg
for more information on this very old algorithm.

Wikipedia https://en.wikipedia.org/wiki/Euclidean_algorithm also has a formal write-up.

Example(s)
euclidGCD(9, 27) == 9
euclidGCD(27, 9) == 9
euclidGCD(3, 1) == 1
 

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
- base case is when either a or b equals 0
- recursive case is to perform division algorithm until we reach the base case
- need to pull the max and min each time
 

🛠️ IMPLEMENT
function euclidGCD(a, b) {
def euclidGCD(a: int, b: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# def euclidGCD(a, b):
#     if a == 0:
#         return b
#     if b == 0:
#         return a
    
#     small = min(a, b)
#     big = max(a, b)

#     # division operation

#     return euclidGCD(big % small, small)

def euclidGCD(a: int, b: int) -> int:
  if b == 0:
    return a
  else:
    return euclidGCD(b, a % b)

print(euclidGCD(196, 180))

print(euclidGCD(9, 27) == 9) 
print(euclidGCD(27, 9) == 9)
print(euclidGCD(3, 1) == 1) 
print(euclidGCD(50, 1) == 1) 
print(euclidGCD(50, 2) == 2)
print(euclidGCD(50, 4) == 2)
print(euclidGCD(100, 50) == 50) 
print(euclidGCD(23, 23) == 23) 
print(euclidGCD(10, 10) == 10) 
print(euclidGCD(31, 19) == 1)
print(euclidGCD(1, 1) == 1)
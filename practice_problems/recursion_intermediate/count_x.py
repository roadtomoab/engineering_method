'''
❓ PROMPT
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
- empty string returns 0 (base case)
- if letter is x, return 1 + countX(rest of string)
- else return countX(rest of string) 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) - iterating over entire string
Space: O(n) - recursion stack of size n
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function countX(word) {
def countX(word: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def countX(word: str) -> int:
    if len(word) == 0:
        return 0
    
    if word[0] == 'x':
        return 1 + countX(word[1:])
    else:
        return countX(word[1:])

print(countX(""))
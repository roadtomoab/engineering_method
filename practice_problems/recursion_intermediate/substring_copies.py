'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

Example(s)
strCopies("catcowcat", "cat", 2) == True
strCopies("catcowcat", "cow", 2) == False
strCopies("catcowcat", "cow", 1) == True
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
- need to go through the string and essentially build a substring
- once we get one, we can add to our count and start from the character after because of overlapping
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n^2) - iterate over whole string for each character potentially
Space: O(n^2) - stack size 
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strCopies(word: str, sub: str, n: int) -> bool:

    if n == 0:
        return True
    
    if len(word) < len(sub):
        return False
    
    if word[0:len(sub)] == sub:
        return strCopies(word[1:], sub, n-1)
    
    return strCopies(word[1:], sub, n)
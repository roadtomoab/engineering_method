'''
❓ PROMPT
Given a string, recursively compute a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a"

- when two chars are next to each other and the same, we need to stick a star in between them
 

🔎 EXPLORE
List your assumptions & discoveries:
- input doesn't have to valid - can be empty string
- string of one character just returns itself no matter what
 

Insightful & revealing test cases:
- "" -> ""
- "x" - > "x"
- "xx" -> "x*x"
- "xy" -> "xy" 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(N)
Space: O(N)

- space will be O(n), since our call stack will be size n (length of string)
- time should also be O(n), since we'll need to iterate over the entire string

- let's think about base case
- should just be none

- need to keep track of pairs essentially, when second one is none that's when we can exit
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function pairStars(word) {
def pairStars(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def pairStars(word: str) -> str:
  if len(word) <= 1:
    return word

  if word[0] == word[1]:
    return str(word[0]) + "*" + pairStars(word[1:])

  return str(word[0]) + pairStars(word[1:])


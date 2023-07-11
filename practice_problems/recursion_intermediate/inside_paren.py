'''
❓ PROMPT
Given a string that contains exactly 1 pair of parentheses, compute recursively a new string made of only the parentheses and their contents, so "xyz(abc)123" yields "(abc)".

Example(s)
parenBit("xyz(abc)123") == "(abc)"
parenBit("x(hello)") == "(hello)"
parenBit("(xy)1") == "(xy)"
 

🔎 EXPLORE
List your assumptions & discoveries:

- assume that there's a parentheses no matter what
- empty parentheses would yield an empty parentheses
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) - iterate entire string
Space: O(n) - call stack of size n
 

📆 PLAN
Outline of algorithm #: 

base case:
- when we hit closing parentheses, add the end and return
- recursive case:
    - have a boolean value turn true when we hit our opener
    - call new value, incrementing string
- we'll use a helper function that takes in our input string, a boolean value, and an index
- we'll have a result string defined outside of helper that we simply add to

 

🛠️ IMPLEMENT
function parenBit(word) {
def parenBit(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def parenBit(word: str) -> str:

    result = ""

    def helper(word, index, open):
        nonlocal result

        if word[index] == ')':
            return result + ')'
        if word[index] == '(':
            open = True
            result += '('
            return helper(word, index + 1, open)
        if open:
            result += word[index]
        return helper(word, index + 1, open)

    return helper(word, 0, False)

print(parenBit("xy(23)"))

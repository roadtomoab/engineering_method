'''
❓ PROMPT
Many teams use a type of tool called a linter to scan code to ensure it follows certain standards and best practices.
One common rule a linter might check for is the depth of nesting of control flow. Functions with many levels of nesting 
are often overly complex, hard to read or modify, and can be bug farms. 
We're going to write a function to determine the depth of control flow for if-statements so that teams will be 
automatically notified if it gets too deep.

In Visual Basic (an old language I hope most of you never need to use), 
if statements are bounded by four keywords: if, elseif, else, and endif. 
Given a sequence of these keywords, return the max nesting depth or -1 if the structure is incorrect.

The structure is incorrect when:
1. The first keyword is anything other than an if.
2. If and endif keywords do not pair up or are out of order.
3. An else or elseif is not inside an if.
4. There are two else blocks in a row.
5. An elseif follows an else at a given level.

Start by implementing this with only if, and endif. Then add support for else. Once that is working, modify the code to support elseif as well.

Example(s)
vbNesting(["if"]) == -1
vbNesting(["endif"]) ==  -1
vbNesting(["if", "endif"]) == 1
vbNesting(["if", "else", "endif"]) == 1
vbNesting(["if", "endif", "if", "endif"]) == 1
vbNesting(["if", "if", "endif", "endif"]) == 2
vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3
vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3

[if, if, if]
 

🔎 EXPLORE
List your assumptions & discoveries:
- start with just if and endif
- think of it like matching brackets (()) ()() a a b b -- a b a b
- assume that if there's no input we return false
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: use a stack
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- check first to see if empty or if first element is if
- use a stack to track corresponding values
- add to stack if not a corresponding value
- top of stack is corresponding value to current value in iteration, pop off stack
- if at the end of our iteration stack is length 0, it's valid
- we'll find length based on the max number of ifs at any given point, track in a counter variable
 

🛠️ IMPLEMENT
function vbNesting(controlFlow) {
def vbNesting(controlFlow: list[str]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def vbNesting(control_flow):
  stack = []
  maxDepth = 0

  for i in range(len(control_flow)):
    nextKeyword = control_flow[i]
    if nextKeyword == "if":
      stack.append("if")
      maxDepth = max(maxDepth, len(stack))
    elif nextKeyword == "endif":
      if len(stack) == 0:
        return -1
      else:
        topKeyword = stack.pop()
    elif nextKeyword == "elseif" or nextKeyword == "else":
      if len(stack) == 0:
        return -1

      topKeyword = stack.pop()
      if topKeyword == "if" or topKeyword == "elseif":
        stack.append(nextKeyword)
      else:
        return -1

  if len(stack) == 0:
    return maxDepth
  return -1

print(vbNesting(["if"]) == -1)
print(vbNesting(["endif"]) ==  -1)
print(vbNesting(["if", "endif"]) == 1)
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3)
print(vbNesting(["if", "endif", "if", "endif"]) == 1)
print(vbNesting(["if", "if", "endif", "endif"]) == 2)
print(vbNesting(["else"]) == -1)
print(vbNesting(["endif", "if"]) == -1)
print(vbNesting(["if", "else", "if", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif", "else", "endif", "endif"]) == -1)
print(vbNesting(["if", "elseif", "elseif", "elseif", "endif"]) == 1)
print(vbNesting(["if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "if", "elseif", "else", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "else", "elseif", "endif"]) == -1)
print(vbNesting(["if", "else", "else", "endif"]) == -1)
        




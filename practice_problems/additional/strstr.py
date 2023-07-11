'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a string, return the index of the first occurrence of a target string. Return -1 if the input string does not contain the target string.

Examples:
• Given a string: "hello", target: "ll" // returns 2
• Given a string: "formation", target: "afor" // returns -1

🔎 EXPLORE
What are some other insightful & revealing test cases?
- can we assume target will never be empty?
- can we also assume given empty string, return -1?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- iterate through string
- if a character matches first character of target
    - slice according to length of target (check if enough chars long enough)
    - check for equivalence
    - if equal, return index
- return -1 (not found)
Time: O(nk)
Space: O(nk)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strstr(inputString: str, target: str) -> int:
    if not inputString:
        return -1

    for i in range(len(inputString)):
        if inputString[i] == target[0]:
            end = i + len(target)
            if end > len(inputString):
                return -1
            sub = inputString[i:end]
            if sub == target:
                return i
    
    return -1

print(strstr("herpes", "pes"))
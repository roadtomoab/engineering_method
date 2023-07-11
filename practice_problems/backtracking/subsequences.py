'''
❓ PROMPT
Define a subsequence of a string "s" to be a list of characters from "s" such that the characters appear in the same order in the list and in "s".

For instance, for the string "abcd", "a", "ab", and "acd" are valid subsequences, whereas "db" is not, since "b" comes before "d" in the original string.

Given an input string, return all subsequences except the empty string.

Example(s)
getAllSubsequences("abc") ==
  ["a", "b", "c", "ab", "ac", "bc", "abc"]
 

🔎 EXPLORE
List your assumptions & discoveries:
 - "" -> ""
 - "a" -> "a"
 - assume that we take in a valid string
 - assume that elements don't have to be unique

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()

- a backtracking approach seems best
    - each time, we decide to add the next letter or not
    - so for a abc, add b don't add b, add c don't add c etc
- what's the time complexity? O(n) or O(n^2)?
- space complexity should be O(n), recursive stack
 

📆 PLAN
Outline of algorithm #:
- we'll need a results array to push our subsequences into
- use a helper function inside our main function
- base case should be when there are no more elements from the string to check
- recursive cases will be either adding, or not adding
- should be able to track with just an index variable for our string
 

🛠️ IMPLEMENT
function getAllSubsequences(word) {
def getAllSubsequences(word: str) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def getAllSubsequences(word: str) -> 'list[str]':

    results = []

    def helper(word, subseq=""):
        nonlocal results

        if len(word) == 0:
            results.append(subseq)
            return

        helper(word[1:], subseq+word[0])
        helper(word[1:], subseq)

    helper(word,"")
    return results

print(getAllSubsequences("abc"))

def getAllSubsequencesNoSlice(word: str) -> 'list[str]':

    results = []

    def helper(word, subseq, i):
        nonlocal results

        if len(word) == i:
            results.append(subseq)
            return
        
        helper(word, subseq, i+1)
        helper(word, subseq+word[i], i+1)

    
    helper(word, "", 0)
    return results

print(getAllSubsequencesNoSlice("abc"))
'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of integers, find all unique triplets (a, b, c) in the array such that their sum equals zero (a + b + c = 0).

Examples:
• Given an array: [1, 2, 0] returns: []
• Given an array: [-1, 0, 1, 0, 1] returns: [[-1, 0, 1]]
• Given an array: [-5, -1, 0, 1, 4, -1] returns: [[-5,1,4], [-1,0,1]]

🔎 EXPLORE
What are some other insightful & revealing test cases?
- if length is less than 0, we can return an empty array
- if no triplets add up until 0, we can return an empty array
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: brute force, have three loops to check all of the triplet combinations
Time: O(n^3) three nested loops
Space: O(n) (result array)

Algorithm 2:
- use a hash map?
                                       
- find all of the complements by getting each pair in the array
- then we just need to go through the array again, checking if the complement exists.  it would make sense to store the pairs as the value for complement key
- push pair + matching array[i] to results array

- what about duplicates? 

time: O(n^2) - need nested loop to get all combinations, then we iterate once more separately to check for complement? or could we do this at the same time?
space: O(n) - creating hash map size n, results array size n 
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def tns(input):
    results = []

    input.sort()

    for i in range(len(input)):
        # skip over repeating numbers - have already done calculation for triplet starting with that number
        if i > 0 and input[i] == input[i-1]:
            continue

        # set pointers
        left = i + 1
        right = len(input) - 1

        # find triplets
        while left < right:
            if input[i] + input[left] + input[right] == 0:
                results.append([input[i], input[left], input[right]])
                left += 1
                right -= 1

                # handle duplicates again
                while left < right and input[left] == input[left-1]:
                    left += 1
                while left < right and input[right] == input[right+1]:
                    right -= 1

            elif input[i] + input[left] + input[right] > 0:
                right -= 1
            else:
                left += 1
    
    return results

print(tns([1, 2, 0]))
'''
❓ PROMPT
You have a long flowerbed in which some plots are planted and others are not. However, new flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty, and 1 means not empty, and an integer *newFlowers*, return true if all *newFlowers* can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example(s)
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Input: flowerbed = [0,0,1], n = 1
Output: true
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume only 1s and 0s
- assume that input flowerbeds are valid when given to you
 

Insightful & revealing test cases:
- [0] 1 -> true - no adjacent spots period, can fill it
- [0] 2 -> false
- [0,0] 1 -> true
- [0,1] 1 -> false
- [0,0,0,0] 3 -> false
- [0,0,0,0,0] 3 -> true
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- iterate through flowerbed
- can only put in a new flower in these spaces:
    - ends with a zero, followed by a zero
    - middles with a zero, surrounded by zeroes
- each time we encounter one of these scenarios, we can decrement n
- if n is > 0 return false, return true otherwise
Time: O(n) - iterating over flowerbed once
Space: O(1) - no extra space needed

can get around this by adding a zero to each end, that way all cases are where a zero is surrounded by zeros
 

📆 PLAN
Outline of algorithm #:

 

🛠️ IMPLEMENT
function canPlantFlowers(flowerbed, newFlowers) {
def canPlantFlowers(flowerbed: list[int], newFlowers: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

import math

def canPlantFlowers(flowerbed: 'list[int]', newFlowers: int) -> bool:

    if newFlowers == 0:
        return True

    flowerbed = [0] + flowerbed + [0]

    for i in range(1, len(flowerbed)-1):

        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            newFlowers -= 1
    
    return newFlowers <= 0

print(canPlantFlowers([0], 1) == True)
print(canPlantFlowers([0], 2) == False)
print(canPlantFlowers([1], 1) == False)
print(canPlantFlowers([0,0], 1) == True)
print(canPlantFlowers([0,0], 2) == False)
print(canPlantFlowers([1,0], 1) == False)
print(canPlantFlowers([0,1], 1) == False)
print(canPlantFlowers([1,1], 1) == False)
print(canPlantFlowers([0,0,0], 1) == True)
print(canPlantFlowers([0,0,0], 2) == True)
print(canPlantFlowers([0,0,0], 3) == False)
print(canPlantFlowers([1,1,1,0,0], 1) == True)
print(canPlantFlowers([1,1,1,0,0], 2) == False)
print(canPlantFlowers([1,1,1,1,1,1,1], 0) == True)
print(canPlantFlowers([1,1,1,1,1,1,1], 1) == False)
print(canPlantFlowers([1,0,0,0,1], 1) == True)
print(canPlantFlowers([1,0,0,0,1], 2) == False)
print(canPlantFlowers([0,0,1], 1) == True)

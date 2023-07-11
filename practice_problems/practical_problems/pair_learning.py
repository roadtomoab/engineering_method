
'''
Chemical Equation Balancing

You have a string s that represents a chemical reaction.

The chemical reaction is a string in the following format: 
    molecule (+ molecule)* = molecule (+ molecule)*, 
    where " * " means any non-negative number of repeats. 
    For example, "A = B", "A = B + C", "A + B + C = D + E + F" are chemical reactions 
    but "X + Y = ", "X = + Z" are not.

A molecule is concatenation of an optional coefficient, a string that represents the concatenation of elements, and their optional coefficents. A coefficent is a positive integer that doesn't exceed 1000, and it represents the number of repeats. For example, "Cu12" means 12 repeats of "Cu" element. "3H2O" means 6 repeats of "H" element and 3 repeats of "O" elements: 3 is a coefficient of the "H2O" molecule, and 2 is a coefficient of the "H" element. The coefficient of the "O" element is absent, which means this element repeats once in each instance of this molecule.

An element is a string that starts with an uppercase English letter, while every other symbol is a lowercase English letter. For example, "A" and "Abc" are elements but "FF" and "hello" is not. "FF" actually indicates that there are 2 repeats of the "F" element. A chemical reaction is considered to be balanced if every element has the same number of repeats on both sides of the chemical reaction. Check whether the given chemical reaction is balanced.
 

EXAMPLE(S)
For s = "2H2 + O2 = 2H2O", the output should besolution(s) = true. Left side: 4 * "H" and "2 * O". Right side: 4 * "H" and "2 * O".

For s = "1000H2O = Au + Ag", the output should besolution(s) = false. Left side: 2000 * "H" and "1000 * O". Right side: 1 * "Ag" and "1 * Au".

- we want to check whether a given chemical reaction is balanced or not 
- rules:
    - plus signs have to make sense
    - coefficient comes after the symbol, number of repeats
    - outside coefficent multiplies everything that comes after integer
    - element has to start with capital letter, and that's the only capital letter 
- balanced if every element has the same number of repeats on both sides

potential edge cases?
- assume that they're semantically valid

brainstorm / outline
- use a dictionary to count occurences on each side
    - increment count for left side, decrement for right, and if any values are greater than 0, return False
    
psuedocode / planning

- split into left and right partitions
- define a dict to count occurences

2H2 + O2 = 2H2O
left = "2H2 + O2 "
right = " 2H20"

- split left and right again by plus sign (if plus sign), get rid of spaces
left = ["2H2", "O2"]

Abc 

- iterate over the left side
    - if first char is number, we'll hold that value and multiply it by all counts afterwards
    - if char is letter, look at coefficent to get count. multiply by outer
    Abc2 - continue to look until we reach a number, or upper bound
         - update key to be as we go 
        - note - check for out of bounds
    - add char and count to frequency dict

- iterate over the right side
    - if first char is number, we'll hold that value and multiply it by all counts afterwards
    - if char is letter, look at coefficent to get count. multiply by outer
        - note - check for out of bounds
    - if not in dict, return False
    - otherwise, subtract count from frequency dict

 

FUNCTION SIGNATURE
is_balanced(s: str) -> bool:
'''
def is_balanced(s: str) -> bool:

    freq = {}

    left, right = s.replace(" ", "").split("=")
    left = left.split("+")
    right = right.split("+")

    for i in range(len(left)):
        j = 0
        chunk = left[i]
        multiplier = 1
        while j < len(chunk):
            if j == 0 and chunk[j].isdigit():
                multiplier = int(chunk[j])
                j += 1
                continue
            if chunk[j].isupper():
                curr_el = chunk[j]
                while j+1 < len(chunk):
                    if chunk[j+1].isalpha():
                        curr_el += chunk[j+1]
                        j += 1
                        continue
                    elif chunk[j+1].isdigit():
                        if curr_el not in freq:
                            freq[curr_el] = int(chunk[j+1]) * multiplier
                        else:
                            freq[curr_el] += int(chunk[j+1]) * multiplier
                        j += 1
            j += 1

    for i in range(len(right)):
        j = 0
        chunk = right[i]
        multiplier = 1
        while j < len(chunk):
            if j == 0 and chunk[j].isdigit():
                multiplier = int(chunk[j])
                j += 1
                continue
            if chunk[j].isupper():
                curr_el = chunk[j]
                while j+1 < len(chunk):
                    if chunk[j+1].isalpha():
                        curr_el += chunk[j+1]
                        j += 1
                        continue
                    elif chunk[j+1].isdigit():
                        if curr_el not in freq:
                            return False
                        else:
                            freq[curr_el] -= int(chunk[j+1]) * multiplier
                        j += 1
                j += 1
    
    





print(is_balanced("2H2 + O2 = 2H2O"))
# print(is_balanced("2H2 + O2 = 2H2O"))
# print(not is_balanced("1000H2O = Au + Ag"))
# print(is_balanced("H2O = H2O"))
# print(is_balanced("2H2O2 = 2H2O + O2"))
# print(not is_balanced("NaCl = Na + Cl2"))
# print(is_balanced("C6H12O6 + 6O2 = 6CO2 + 6H2O"))
# print(is_balanced("12H2O = 12H2 + 6O2"))
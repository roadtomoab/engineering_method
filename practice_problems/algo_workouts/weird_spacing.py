'''
Given an array of words and a max length per line, return an array of strings where each string represents a fully justified line. A fully justified line means that the first letter and last letter in the line should be a letter and not a space, and extra spaces are distributed as evenly as possible.

For the last line of text, it should be left-justified, and no extra space is inserted between words.
 
5 - 2 2 1

EXAMPLE(S)
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], k = 16

returns
["the  quick brown", // (2 spaces, 1 space)
"fox  jumps  over", // (2 spaces, 2 spaces)
"the lazy dog    "]  // (left justify, fill the end with 4 spaces)
 
1. Fit as many words as possible - greedy approach
2. word.length <= k

loop through array (S)

line_length = 0
result = []
curr_line = []
curr_char = 0;
for each word in array:
    line_length = length of word + curr_line.length + curr_char
    if line_length > K:
        number of spaces = K - curr_char
        justify(numberOFSpaces, curr_line)
        result.append(curr_line)
        curr_line = [word]
    else:
        curr_line.append(word)
        curr_char += word.length
if curr_line:
    result.append(curr_line) 
    
    
jusify(spaces, curr_line)

result = ""
if len(curr_line) == 1:
    result.push(curr_line[0] + spaces);
else
    
    5, 3

    2, 2, 1

    spaceIndex % nunber of section
    0 % 3-> 0 -> curr_char[i % numberOfSection] += " "
    1 % 3-> 1
    2 % 3-> 2
    3 % 3-> 0
    4 % 3-> 1
    result.push(''.join(curr_line))

'''
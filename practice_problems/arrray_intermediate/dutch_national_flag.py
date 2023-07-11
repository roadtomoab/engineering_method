'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an array of 0s, 1s, and 2s, sort them in-place in ascending order.

Examples:
• Given an array: [2, 1] // returns [1, 2]
• Given an array: [0, 2, 1, 0, 1, 2] // returns [0, 0, 1, 1, 2, 2]

🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def dnf(nums):
    # count occurences in an array
    freq = {
        0: 0,
        1: 0,
        2: 0
    }

    for num in nums:
        if num == 0:
            freq[0] += 1
        elif num == 1:
            freq[1] += 1
        elif num == 2:
            freq[2] += 1
    
    index = 0
    for key, value in freq.items():
        for i in range(value):
            nums[index] = key
            index += 1
    
    return nums

def dnf_one_pass(nums):
    # initialize three pointers to keep track of the boundaries
    low = 0    # points to the first element of the sub-array of 0s
    mid = 0    # points to the first unexamined element
    high = len(nums) - 1    # points to the last element of the sub-array of 2s

    # iterate through the array from left to right
    while mid <= high:
        # if the current element is 0, swap it with the element at index low and increment both low and mid
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]    # swap the elements
            low += 1    # increment the low pointer
            mid += 1    # increment the mid pointer
        # if the current element is 1, leave it in place and increment mid
        elif nums[mid] == 1:
            mid += 1    # increment the mid pointer
        # if the current element is 2, swap it with the element at index high and decrement high
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]    # swap the elements
            high -= 1    # decrement the high pointer
            # do not increment the mid pointer, as the swapped element needs to be examined again

    return nums

array = [1, 1, 1, 2, 0, 1, 2, 2, 0]
print(dnf(array))
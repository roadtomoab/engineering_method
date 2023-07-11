'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class.

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

cache:



Examples:
See test cases.

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

class LRUCache:
    def __init__(self):
        self.capacity = 3
    
    def get()

    def put()

# let's run through an example
# I put three items in the cache 1,2,3. lru is 1
# I access 1. 2,3,1 now. lru is 2
# I access 3. 2,1,3 now. lru is 2 still
# I add 4. 1,3,4 now since capacity is three and we get rid of lru

# we'll probably need a hash map to keep track of the key value pairs
# then we'll also have a list that keeps track of the order in the cache

# most recent 1 <-> 2 <-> 3 least recent
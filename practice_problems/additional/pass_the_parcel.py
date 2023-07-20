'''
❓ PROMPT
In this game, a group of players stands in a circle and passes a parcel around.
When the game starts, a player is chosen to hold the parcel.
The players then pass the parcel to their adjacent player in clockwise order.
At a random point in time, a timer goes off, and the player holding the parcel is removed from the circle.
The passing continues until only one player is left.

Example(s)
We have a list  ["Alice", "Bob", "Charlie", "David", "Eve"]
Assume we have a timer value of 3.
Iteration 1: David removed
Iteration 2: Charlie removed
Iteration 3: Eve removed
Iteration 4: Bob Removed
Winner: Alice.
 

🔎 EXPLORE
List your assumptions & discoveries:
- timer value can't be negative
- assume valid inputs for names
 

Insightful & revealing test cases:
- timer is 0 - eve would be the winner, player who holds parcel immediately eliminated
- timer is greater than length of list - same as timer minus length of list
- timer is length of list - same as 0

 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- have a list represent a circle
- while len of circle is greater then 1
    - pass the parcel m (timer) number of times
        - reorder the list so that parcel holder is always at the front
    - pop off parcel holder one we reach the timer
Time: O(m*n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function passTheParcel(players, timer) {}
def passTheParcel(players, timer):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def passTheParcel(players: 'list[int]', timer: int) -> str:

    circle = players.copy()

    while len(circle) > 1:
        for _ in range(timer):
            circle.append(circle.pop(0))
        circle.pop(0)
    
    return circle[0]

players = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Test Case 1: Timer less than the number of players
timer1 = len(players) - 1
winner1 = passTheParcel(players, timer1)
print(winner1 == "Bob")

# Test Case 2: Timer equal to the number of players
timer2 = len(players)
winner2 = passTheParcel(players, timer2)
print(winner2 == "David")

# Test Case 3: Timer greater than the number of players
timer3 = len(players) + 2
winner3 = passTheParcel(players, timer3)
print(winner3 == "Alice")

# Test Case 4: Timer less than 1
timer4 = 0
winner4 = passTheParcel(players, timer4)
print(winner4 == "Eve")
'''
❓ PROMPT
A dance studio is holding a Tango lesson tonight involving 2 half-hour sessions. The studio is creating a plan to pair dancers in the second session with a different partner from the first session. Given a list of Tango pairs for each session, determine if the studio will pair up any partners twice.

This problem aims to familiarize you with storing and retrieving information from data structures to create a minimal algorithm. In this instance, the Engineering Method is valuable because it helps you arrive at a more optimal algorithm than brute force.

As a follow-up, how would you write an algorithm to detect repeated pairs in 3 sessions, in any number of sessions? How would you write an O(N) time algorithm to determine how often the matcher created each pair? Again, it should count pairs in reversed order as the same pair.

Example(s)
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
hasRepeatTangoPartner(session1, session2) == False

session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
hasRepeatTangoPartner(session1, session2) == True

Jack and Daniels have been partnered up on both sessions.
 

🔎 EXPLORE
List your assumptions & discoveries:
- assume that order doesn't matter - Jack, Daniels and Daniels, Jack should still be the same
- assume that that there's only two pairs per session to start
- assume that there are no mistakes in pairing for each session (alice isn't listed twice in session1 array)
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- for each pair in session one, check against each pair in session 2
- would involve a nested loop, and would involve checking the flipped version against each
Time: O(n^2)
Space: O(n) - n arrays of length 2, to have the flipped pair as well

Algorithm 2:
- use a hash map
- iterate through first session
    - put regular and reversed into hash map
- iterate through second session
    - if first name is a key
        - return true if second name matches value
    - if second name is a key
        - return true if first name matches value
- return false at the end, means we have no matches
Time: O(n) - iterating through each session of same size n separately
Space: O(n) - creating hash map of size n (actually 2n, but it simplifies)
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
def hasRepeatTangoPartner(firstSession: list[str], secondSession: list[str]) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def hasRepeatTangoPartner(firstSession: 'list[str]', secondSession: 'list[str]') -> bool:

    pairChecker = {}

    for session in firstSession:
        if session[0] not in pairChecker:
            pairChecker[session[0]] = session[1]
        if session[1] not in pairChecker:
            pairChecker[session[1]] = session[0]
    
    for session in secondSession:
        if session[0] in pairChecker:
            if pairChecker[session[0]] == session[1]:
                return True
        if session[1] in pairChecker:
            if pairChecker[session[1]] == session[0]:
                return True
    
    return False

# swapped ordering shouldn't affect the correctness
session1 = [["Alice", "Baxter"]]
session2 = [["Baxter", "Alice"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# disjoint list
session1 = [["Alice", "Baxter"]]
session2 = [["Charles", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# partner mixing
session1 = [["Alice", "Baxter"], ["Charles", "Davis"]]
session2 = [["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# more partner mixing
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
print(hasRepeatTangoPartner(session1, session2) == False)

# 1 overlap
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# overlap with flipped partners
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Daniels", "Jack"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2) == True)

# no overlap
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jono", "Paavo"], ["Zoe", "Angus"], ["Oliver", "Pixel"]]
print(hasRepeatTangoPartner(session1, session2) == False)
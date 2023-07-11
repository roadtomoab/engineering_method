'''
You don't have to get through all of these in the session. Instead, aim for an optimal learning experience.
Stacks and queues are often used as lists of things to do or items to be processed in a particular order. In this series of exercises, the goal is practice using stacks and queues to manage work to be done while searching through friend connections.

Given a dictionary of friend lists:

    1) Given a person's name, return a list of all of the friends of their friends (2nd order friends)
    2) Given a person's name and a positive number, n, greater than 0, return the nth order friends. For n = 1, that is the person's direct friends. For n = 2, this gives the same result as the first problem.
    3) Given two people's names, return the distance between them in friend connections, their Kevin Bacon number?

All of these problems take as input a dictionary where the keys are someone's name and the value for each is a list of their friend's names:

{
  "Daniel": ["Mike", "Sophie", "James", "Tony"],
  "Mike": ["Daniel", "James", "Luke"],
  "Tony": ["Daniel", "Sophie"],
  "Sophie": ["Michael", "Daniel", "Tony", "Eun Ji"],
  /* etc */
}

'''
from collections import deque

# 1) Given a person's name, return a list of all of the friends of their friends (2nd order friends)

def second_order_friends(friends, name):
    # for each of name's friends, we need to go into the dictionary and grab all of their friends

    # we'll use a stack, add friends of name to stack
    stack = friends[name]
    friend_list = set()

    while stack:
        current_friend = stack.pop()
        if current_friend in friends:
            current_list = friends[current_friend]
            friend_list.update({value for value in current_list})
            # for name in current_list:
            #     friend_list.add(name)
    
    return friend_list

def second_order_friends(friends, name):

    queue = deque(friends[name])
    friend_list = set()

    while queue:
        current_friend = queue.popleft()
        if current_friend in friends:
            current_list = friends[current_friend]
            friend_list.update({value for value in current_list})
    
    return friend_list



friends = {
  "Daniel": ["Mike", "Sophie", "James", "Tony"],
  "Mike": ["Daniel", "James", "Luke"],
  "Tony": ["Daniel", "Sophie"],
  "Sophie": ["Michael", "Daniel", "Tony", "Eun Ji"]
}

# print(second_order_friends(friends, "Daniel"))


# 2) Given a person's name and a positive number, n, greater than 0, return the nth order friends. For n = 1, that is the person's direct friends. For n = 2, this gives the same result as the first problem.

def nth_order_friends(friends, name, n):
    friend_list = set()
    queue = deque([name])
    level = 0

    while queue:
        if level == n:
            friend_list |= set(queue) # add all remaining friends at nth degree
            break
        for i in range(len(queue)):
            current_friend = queue.popleft()
            if current_friend in friends:
                queue += friends[current_friend]
        level += 1
    return friend_list

def nth_order_friends_recursive(friends, name, n):
    if n == 1:
        return set(friends[name]) if name in friends else set()
    
    friend_list = set()
    if name in friends:
        for friend in friends[name]:
            nth_order = nth_order_friends(friends, friend, n-1)
            friend_list |= nth_order
    return friend_list


print(nth_order_friends(friends, "Daniel", 2))
print(nth_order_friends_recursive(friends, "Daniel", 2))

# 3) Given two people's names, return the distance between them in friend connections, their Kevin Bacon number?

def find_distance(friends, name1, name2):

    q = deque([name1])
    level = 0

    while q:
        for i in range(len(q)):
            current_friend = q.popleft()

            if current_friend == name2:
                return level
            
            if current_friend in friends:
                friends_to_add = set(friends[current_friend])
                q.extend(friends_to_add)
        level += 1
    
    return "no connection"

# print(find_distance(friends, "Mike", "Tony"))



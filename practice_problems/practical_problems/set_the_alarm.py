'''
❓ PROMPT
You're exhausted after a long day and heading to bed, but you still have to set the alarm clock on your phone. You already have one you set the day before, so all you have to do is update it.

To set your alarm, the hours and minutes are set independently, each by scrolling upwards or downwards. One shift changes an hour or minute value by one, up or down. The values are organized cyclically, which means that dragging 0 minutes downwards turns it into 59, and dragging 59 upwards turns it into 0 (similarly, 0 hours can become 23 in one shift and vice versa).

Given the time of the previous alarm and the new desired time, what is the minimum number of scroll moves to set the new time?

Example(s)
For setTime = "07:30" and timeToSet = "08:00", the output should be
minScrollToSet(oldTime, newTime) = 31.

Shifting hours upwards once will change the alarm to "08:30", and shifting minutes 30 times downwards will change it to "08:00".

'''

# two ways to get to one number, we essentially have to find the minimum

# for example, to get from 7 to 8, we either move up 1, or down 23
# need to handle changing 0 to 24 and vice versa 
# same thing with minutes, just a wider range


# does the instance where we're moving 12 hours, or 30 minutes change anything? I don't think so

# basic approach

# split our input strings to grab hours and minutes of set times and time to set

# how do we find each? downwards take abs value of difference, upwards do 24 minus max + min
# take minimum of these two values and add it to our resultf

def minScrollToSet(set_time, time_to_set):
    result = 0

    hour_a, mins_a = set_time.split(":")
    hour_a = int(hour_a)
    mins_a = int(mins_a)

    hour_b, mins_b = time_to_set.split(":")
    hour_b = int(hour_b)
    mins_b = int(mins_b)

    downward_hour = abs(hour_a - hour_b)
    min_hour = min(hour_a, hour_b)
    max_hour = max(hour_a, hour_b)
    upward_hour = 24 - max_hour + min_hour

    downward_min = abs(mins_a - mins_b)
    min_mins = min(mins_a, mins_b)
    max_mins = max(mins_a, mins_b)
    upward_mins = 60 - max_mins + min_mins

    result += min(downward_hour, upward_hour) + min(downward_min, upward_mins)

    return result

print(minScrollToSet("7:00", "6:31") == 30)
print(minScrollToSet("7:00", "6:25") == 26)
print(minScrollToSet("7:30", "8:00") == 31)
print(minScrollToSet("7:00", "8:00") == 1)
print(minScrollToSet("8:00", "8:00") == 0)
print(minScrollToSet("6:59", "7:01") == 3)
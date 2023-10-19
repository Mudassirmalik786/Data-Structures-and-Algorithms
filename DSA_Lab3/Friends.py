# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:49:13 2023

@author: HP
"""

'''
# Pseudo code
friendSlower(Input):
    Initialize an empty list to store the pairs
    For each user i in Input:
        For each user j after i in Input:
            If user i and user j overlap in time:
                Add the pair (i, j) to the list
    Return the list of pairs

'''

def friendSlower(Input):
    pairs = []
    n = len(Input)
    
    for i in range(n):
        for j in range(i+1, n):
            if Input[i][1] >= Input[j][0] and Input[j][1] >= Input[i][0]:
                pairs.append((i+1, j+1))
    
    return pairs

# Example usage 
Input = [[1,4],[2,5],[7,9],[9,10],[6,10]]
result_slower = friendSlower(Input)
print("Pairs of users with overlapping time (O(n^2)):", result_slower)

'''
Pseudo code
friendsFaster(Input):
    Initialize an empty list to store the pairs
    Initialize an empty list to store the events (start or end times)
    For each user (start, end) in Input:
        Add the event (start, 'start') to the list of events
        Add the event (end, 'end') to the list of events
    Sort the list of events by time
    Initialize a variable 'count' to keep track of the number of users present
    For each event (time, type) in the sorted events:
        If type is 'start':
            Increment the count of users
        Else:
            Decrement the count of users
            If count is greater than or equal to 2:
                Add pairs of users using the count (countC2) to the list of pairs
    Return the list of pairs
'''

def friendsFaster(Input):
    events = []
    for i, (start, end) in enumerate(Input):
        events.append((start, 'start', i))
        events.append((end, 'end', i))
    
    events.sort(key=lambda x: (x[0], x[1]))  # Sort by time, and 'start' events before 'end' events
    
    pairs = []
    count = 0
    
    for time, event_type, user in events:
        if event_type == 'start':
            count += 1
        else:
            count -= 1
            if count >= 2:
                for i in range(count-1):
                    pairs.append((user+1, events[-i-2][2]+1))  # Adding 1 to make indices 1-based
    
    return pairs

# Example usage
Input = [[1,4],[2,5],[7,9],[9,10],[6,10]]
result_faster = friendsFaster(Input)
print("Pairs of users with overlapping time (O(n log(n))):", result_faster)

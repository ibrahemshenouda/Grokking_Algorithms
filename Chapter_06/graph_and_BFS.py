#!/usr/bin/python3
from collections import deque

# implement graph in hash table "dictionary"
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# search with any thing you need here
def person_is_seller(name):
    return name[-1] == 'm'

# BFS algorithm


def search(name):
    # to sort graph by levels (first in first out)
    search_queue = deque()
    # node start from to search
    search_queue += graph[name]
    # sort visited nodes to avoid infinite loops
    searched = set()
    while search_queue:  # while set is not empty
        person = search_queue.popleft()  # start from first element in
        if not person in searched:  # check element visited or not
            if person_is_seller(person):  # search method
                print(person + " is a mango seller!")
                return True  # if exist finish
            else:
                # add this node children to search in
                search_queue += graph[person]
                # if not add this node to searched elements
                searched.add(person)
    return False


search("you")  # start node

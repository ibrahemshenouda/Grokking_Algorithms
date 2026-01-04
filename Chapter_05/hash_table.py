#!/usr/bin/python3

# Hash Tables
# dictionary is a Hash tables
# Fast in search
# used to prevent duplicate
# used as a cache in websites

voted = {}


def check_voter(name):
    if name in voted:
        print("Kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


check_voter("tom")
check_voter("mike")
check_voter("tom")
print(voted)

#!/usr/bin/python3

def countdown(i):
    print(i)
    if i <= 1:              #Base case
        return
    else:
        countdown(i-1)      #Recursive case


countdown(5)
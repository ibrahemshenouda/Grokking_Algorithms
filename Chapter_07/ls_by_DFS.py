#!/usr/bin/python3
from os import listdir
from os.path import isfile, join


def printnames(start_dir):
    for file in sorted(listdir(start_dir)):
        fullpath = join(start_dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames(fullpath)


printnames("Chapter_04")

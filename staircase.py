import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = n
    hashtag = 0
    space_symbol = " "
    hastag_symbol = "#"
    while (space != 0):
        space -= 1
        hashtag += 1
        print(space * space_symbol + hashtag * hastag_symbol)

if __name__ == '__main__':
    n = int(input())

    staircase(n)

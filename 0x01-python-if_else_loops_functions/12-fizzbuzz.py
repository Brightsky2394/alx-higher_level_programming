#!/usr/bin/python3
def fissbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FissBuzz", end='')
        elif x % 3 == 0:
            print("Fiss", end='')
        elif x % 5 == 0:
            print("Buzz", end='')
        else:
            print(x, end='')
        print(" ", end='')

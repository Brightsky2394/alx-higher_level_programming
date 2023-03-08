#!/usr/bin/python3
def fissbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FissBuzz", end='')
        elif i % 3 == 0:
            print("Fiss", end='')
        elif i % 5 == 0:
            print("Buzz", end='')
        else:
            print(i, end='')
        print(" ", end='')

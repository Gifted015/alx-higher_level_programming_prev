#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            print("Fizz", end="")
            if x % 5 != 0:
                print(" ", end="")
                continue
        if x % 5 == 0:
            print("Buzz", end=" ")
            continue
        else:
            print(x, end=" ")

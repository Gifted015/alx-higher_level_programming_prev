#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x  < y:
            print("{}{}".format(x, y), end = "")
            if ((x * 10) +  y) != 89:
                print(", ", end = "")
            else:
                print("\n")
                break

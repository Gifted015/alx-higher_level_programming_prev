#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a == 1:
        print("{} argument".format(a), end="")
    else:
        print("{} arguments".format(a), end="")

    if (a) == 0:
        print(".")
    else:
        print(":")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

#!/usr/bin/python3
def safe_print_integer(value):
    try:
        temp = int(value)
        print("{:d}".format(temp))
        return True
    except (ValueError, TypeError):
        return False
